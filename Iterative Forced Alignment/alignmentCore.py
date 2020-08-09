import os
import sys

import json
import threading
import logging
import shutil

from pydub import AudioSegment
from aeneas.task import Task
from aeneas.executetask import ExecuteTask

path = sys.argv[5]
logfile = sys.argv[6]

def iterative_segmentation_core_(folder, text_path, process_path, format_):
    print(folder + " in process")
    result = False
    process_aeneas_map_before(process_path, format_)
    try:
        while not result:
            result = alignment(text_path, process_path, format_)
        print(folder + " finished")
        add_to_finish_list(folder)
        os.system("mv " + text_path + " " + "finished/")
    except:
        add_to_failed_list(folder)

def add_to_start_list(content):
    with open(logfile, "a+") as f:
        f.write(content + " started")

def add_to_finish_list(content):
    with open(logfile, "a+") as f:
        f.write(content + " finished\n")

def add_to_failed_list(content):
    with open(logfile, "a+") as f:
        f.write(content + " failed\n")
    # remove_failed_folder(content)
    
def remove_failed_folder(content):
    folder = path + '/' + content
    if os.path.exists(folder):
        shutil.rmtree(folder)

def remove_three(content):
    file_path = path + '/' + content + '/' + content

    txt_file = file_path + '.txt'
    if os.path.exists(txt_file):
        os.remove(txt_file)

    ss_file = file_path + '_ss.txt'
    if os.path.exists(ss_file):
        shutil.rmtree(ss_file)

    mp3_file = file_path + '.mp3'
    if os.path.exists(mp3_file):
        shutil.rmtree(mp3_file)

    del file_path, txt_file, ss_file, mp3_file

def alignment(text_path, process_path, format_):
    # Use Aeneas produce duration map
    process_aeneas_map(process_path, format_)

    # Get last paragraph of the text
    last_paras = open_json_return_last_para(process_path)

    # Get speaker of last paragraph
    last_speaker = open_ss_return_last_speaker(process_path)

    # Check if speaker is in management team
    is_v = is_vip(last_speaker)

    last_paras_id = ''.join(last_paras['id'])
    last_paras_begin = float(last_paras['begin'])
    last_paras_end = float(last_paras['end'])
    last_paras_lines = ''.join(last_paras['lines'])

    if is_v:
        append_text(text_path, last_paras_lines + '\n')
    else:
        pass

    slice_audio(is_v, process_path, format_, last_paras_id, last_paras_begin, last_paras_end)

    double_cut(process_path, last_paras_lines)

    return last_paras_begin < 1.0
        
def append_text(process_path, content):
    process_path += '/text.txt'
    os.makedirs(os.path.dirname(process_path), exist_ok=True)
    with open(process_path, "a+") as f:
        try:
            f.write(content)
        except IOError:
            print("Saving text failed. A")

def process_aeneas_map_before(filepath_, format_):
    # create Task object
    config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = filepath_ + '.' + format_
    task.text_file_path_absolute = filepath_ + ".txt"
    task.sync_map_file_path_absolute = filepath_ + "_orginal.json"

    # process Task
    ExecuteTask(task).execute()

    # output sync map to file
    task.output_sync_map_file()


# Produce json Aeneas map
def process_aeneas_map(filepath_, format_):
    # create Task object
    config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = filepath_ + '.' + format_
    task.text_file_path_absolute = filepath_ + ".txt"
    task.sync_map_file_path_absolute = filepath_ + ".json"

    # process Task
    ExecuteTask(task).execute()

    # output sync map to file
    task.output_sync_map_file()


# Read json slices, return last paragraph 
def open_json_return_last_para(filepath_):
    json_path = filepath_ + ".json"
    with open(json_path) as json_file:
        json_data = json.load(json_file)
        # print(json_data['fragments'][-1])
        # json_file_print(json_data)
        return json_data['fragments'][-1]


# Get spekaer from speech sequence
def open_ss_return_last_speaker(filepath_):
    speaker_path = filepath_ + "_ss.txt"
    with open(speaker_path) as ss:
        return ss.read().splitlines()[-1]


# Is input speaker is from management team
def is_vip(last_speaker):
    name = get_name(last_speaker)
    if 'vp' in name or 'VP' in name or 'President' in name or 'CEO' in name or 'CFO' in name:
        return True
    else:
        return False


def get_name(last_speaker):
    name = ""
    found_first = False
    for each in last_speaker:
        if each == '(' and not found_first:
            found_first = True
        elif each == ')' and found_first:
            return name
        else:
            name += each

# align audio
def slice_audio(save_audio, process_path, format_, output_id, start, end):
    audio_path = process_path + '.' + format_
    audio = AudioSegment.from_file(audio_path, format=format_)
    start = int(start * 1000)
    end = int(end * 1000)

    # print('start: ' + str(start) + ' end: ' + str(end) + ' audio length: ' + str(len(audio)))

    if int(end) < len(audio):
        end = len(audio)
    slice_length = end - start
    chunk = audio[-slice_length:]

    # print('start: ' + str(start) + ' end: ' + str(end) + ' audio length: ' + str(len(audio)) + ' chunk length: ' + str(len(chunk)))

    if save_audio:
        with open(process_path + '_' + output_id + ".mp3", "wb") as f:
            chunk.export(f, format="mp3")
    
    if start < 1000:
        pass
    else:
        audio = audio[:start]
        with open(audio_path, "wb") as g:
            audio.export(g, format=format_)


# speech sequence 和 原文本 remove 已经切片过的
def double_cut(filepath, sentence):
    cut_ss_txt(filepath, sentence)
    cut_txt(filepath, sentence)


def remove_previous(file):
    if os.path.exists(file):
        os.remove(file)


def cut_ss_txt(filepath, sentence):
    filepath += "_ss.txt"
    new_content = ""
    with open(filepath) as ss:
        for each in ss:
            if ') :  ' + sentence in each or ') : ' + sentence in each:
                # print("removing with name: " + sentence)
                new_content += ''
            elif each.endswith(sentence):
                new_content += each[:-len(sentence)]
            else:
                new_content += each
    write_new_file(filepath, new_content)


def cut_txt(filepath, sentence):
    filepath += ".txt"
    new_content = ""
    with open(filepath) as f:
        for each in f:
            if sentence not in each:
                new_content += each
    write_new_file(filepath, new_content)


def write_new_file(output_path, content):
    remove_previous(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        try:
            f.write(content)
        except IOError:
            print("Saving {output_path} failed. W")

# Function and whole file take 6 arguments in total from scripts
# sys.argv[1] : Current conference call folder name
# sys.argv[2] : Current conference call text path 
# sys.argv[3] : Current conference call audio path 
# sys.argv[4] : Input Audio format (Tried pydub didn't work with m4a, better with mp3)
# sys.argv[5] : Current dataset folder name
# sys.argv[6] : log file name

# Expect folder structure:
# Dataset Folder --> Conference call folders --> Conference_Call_Folder_Name.txt     Text only
#                                                Conference_Call_Folder_Name_ss.txt  Speech Sequence
#                                                Conference_Call_Folder_Name.mp3     Conference call audio

iterative_segmentation_core_(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

