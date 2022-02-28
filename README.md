# Automatic Scoring of Phonological Distance

The evaluation of phonemic performance in aphasia reveals deficits in spoken language and can facilitate the design of targeted treatments. Nevertheless, manual scoring of phonological performance is time-consuming, laborious, and error prone. Here we provide a code that scores phonological errors based on the normalized Damerau–Levenshtein distance, for both words and non words (see below on how to modify it for languages other than English).

# Updates 
02/27/2022

The scoring algorithm will now provide two columns:
- phonological_score: this provides phonological distance between the target and the response (the standard output).
- phonological_score_lemma: this provides the phonological distance between the lemmas. 

# Notes
The alogirithm deals at the moment with one word responses; if the response is a multiword response the phonological distance will include all words of the response in the calculation. You might not want this. 

 # Contact:
 Please do not hesitate to contact me, if you need assistance and I will do my best to respond.  
 
 email: themistocleous@gmail.com
 


# Using the code

## Prerequisites

1. Install espeak, a free open source text to speech software: http://espeak.sourceforge.net
2. Install Anaconda with Python 3: https://www.anaconda.com/products/individual

The required packages pandas, scipy, and numpy, will be installed automatically.

## Data Preparation for analysis

1. You will need a datafile in csv format with three columns titled: **target**, **response**. 


| target | response
| - | - | - |
| bird | berd
| table | taple
| dog | tok
| grace | gaze 

If you there are other columns in the excel file these will not be deleted during the process. However, the order of rows might change so, it is a good practice to have an ID column to function as an index, so that you can sort the excel to its original form.

2. Place the file with the data, at the folder that contains the code.
3. Open the Terminal and cd to the directory that contains the code and run the following command

`python phonology.py -i data.csv -o output.csv 

Above I assume that your data file is titled data.csv and the output file is called output.csv. You can name these files as you like but they need to be in a csv format. A file labelled output.csv will be created in the same location.

## Using the code in other languages

You can use the same code in languages other than American English, you will need to modify, and change the language "en-us" to your own language (shown in column Language in the following table). For example if you want to score words in German you will need to modify

p = subprocess.run(["espeak", "-q", "--ipa", "-v", "en-us"]

to 

p = subprocess.run(["espeak", "-q", "--ipa", "-v", "de"]

Do not forget to save the file after you make the change.


# Help and support

Please do not hesitate to contact me if you get into problems running the code, or if you have questions, suggestions, etc. If you use the code do not forget to cite the paper Themistocleous et al. 2020.


# Cite

**Themistocleous, Charalambos** (2021). A Tool for Automatic Scoring of Phonological distance. https://github.com/themistocleous/phonology_scoring_app.
