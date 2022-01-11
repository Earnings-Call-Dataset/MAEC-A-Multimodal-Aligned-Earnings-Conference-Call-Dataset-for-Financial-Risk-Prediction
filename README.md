# MAEC: A Multimodal Aligned Earnings Conference Call Dataset for Financial Risk Prediction

In the area of natural language processing, various financial datasets have informed recent research and analysis including financial news, financial reports, social media, and audio data from earnings calls. We introduce a new, large-scale multi-modal, text-audio paired, earnings-call dataset named MAEC, based on S&P 1500 companies. We describe the main features of MAEC, how it was collected and assembled, paying particular attention to the text-audio alignment process used. We present the approach used in this work as providing a suitable framework for processing similar forms of data in the future.  The resulting dataset is more than six times larger than those currently available to the research community and we discuss its potential in terms of current and future research challenges and opportunities.

## MAEC Dataset

### Transcripts along with the low-level audio features (Total 147.7 MB)

Each folder named in the format of **YearMonthDay_CompanyCode**. There are two files in each folder:
1. Transcripts text file, named as **text.txt**.
2. Low-level audio features: **features.csv**.

### High-level features (Total 59 GB)

We produced and released high-level (mfcc feature) audio features files, named as **CompanyCode_YearMonthDay-OrderNumber.npy**. Click [here](https://drive.google.com/file/d/1yXLv1r5n35s4Nf7kvP96RSPLKyR-ZeUT/view?usp=sharing) to download.


## Iterative Forced Alignment Core Code

In the **Iterative Forced Alignment** folder, we released our code for text-audio segmentation. 

### Prerequisites

Python version and packages required to install for execute the code.

```
Python 3.5
Pydub
Aeneas
FFMPEG
```

### How to execute the code

Please run a caller program to pass parameters into the execution of code. There are 8 parameters to be set up in total.

Example use case:

```
python3.5 alignmentCore.py FolderPath(CompanyCode_YearMonthDay) TextPath(WorkDirectory/CompanyCode_YearMonthDay) AudioPath(WorkDirectory/CompanyCode_YearMonthDay/CompanyCode_YearMonthDay) AudioFormat(Eg."mp3") WorkDirectory LogFileName(Eg."log1.txt")
```

# Citation

```bibtex
@inproceedings{CIKM2020MAEC,
author = {Li, Jiazheng and Yang, Linyi and Smyth, Barry and Dong, Ruihai},
title = {MAEC: A Multimodal Aligned Earnings Conference Call Dataset for Financial Risk Prediction},
year = {2020},
isbn = {9781450368599},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3340531.3412879},
doi = {10.1145/3340531.3412879},
abstract = {In the area of natural language processing, various financial datasets have informed recent research and analysis including financial news, financial reports, social media, and audio data from earnings calls. We introduce a new, large-scale multi-modal, text-audio paired, earnings-call dataset named MAEC, based on S&amp;P 1500 companies. We describe the main features of MAEC, how it was collected and assembled, paying particular attention to the text-audio alignment process used. We present the approach used in this work as providing a suitable framework for processing similar forms of data in the future. The resulting dataset is more than six times larger than those currently available to the research community and we discuss its potential in terms of current and future research challenges and opportunities. All resources of this work are available at https://github.com/Earnings-Call-Dataset/},
booktitle = {Proceedings of the 29th ACM International Conference on Information &amp; Knowledge Management},
pages = {3063–3070},
numpages = {8},
keywords = {multimodal aligned datasets, earnings conference calls, financial risk prediction},
location = {Virtual Event, Ireland},
series = {CIKM '20}
}
```


# Terms Of Use

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This dataset and iterative forced alignment code is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

# Acknowledgments

* The research project was supported by Science Foundation Ireland (SFI) under Grant Number SFI/12/RC/2289_2.
