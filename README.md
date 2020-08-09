# MAEC: A Multimodal Aligned Earnings Conference Call Dataset for Financial Risk Prediction

In the area of natural language processing, various financial datasets have informed recent research and analysis including financial news, financial reports, social media, and audio data from earnings calls. We introduce a new, large-scale multi-modal, text-audio paired, earnings-call dataset named MAEC, based on S&P 1500 companies. We describe the main features of MAEC, how it was collected and assembled, paying particular attention to the text-audio alignment process used. We present the approach used in this work as providing a suitable framework for processing similar forms of data in the future.  The resulting dataset is more than six times larger than those currently available to the research community and we discuss its potential in terms of current and future research challenges and opportunities.

## MAEC Dataset

### Transcripts along with the low-level audio features

Each folder named in the format of **YearMonthDay_CompanyCode**. There are two files in each folder:
1. Transcripts text file, named as **text.txt**.
2. Low-level audio features: **features.csv**.

### High-level features

In the **MFCC-features** folder, we produced and released high-level (mfcc feature) audio features files, named as **CompanyCode_YearMonthDay-OrderNumber.npy**.


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

Write a caller program to pass parameters into the execution of code. This code takes 8 parameters in total.

Example of how to call it:

```
python3.5 alignmentCore.py FolderPath(CompanyCode_YearMonthDay) TextPath(WorkDirectory/CompanyCode_YearMonthDay) AudioPath(WorkDirectory/CompanyCode_YearMonthDay/CompanyCode_YearMonthDay) AudioFormat(Eg."mp3") WorkDirectory LogFileName(Eg."log1.txt")
```

# Terms Of Use



# Acknowledgments

* This research was supported by Science Foundation Ireland (SFI) under Grant Number SFI/12/RC/2289_2

