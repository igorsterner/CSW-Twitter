# German-English Code-switching

This project implements a method to identified Code-switched German-English tweets automatically, as useful for the development of a new larger scale German-English Code-switching dataset. 

A report was written in German for this project and is available in the docs directory as a PDF. A translation in English will shortly also be available.

## Results

A brief overview of the results of this project is available in the results.md file in this repo

## Requirements

```bash
pip install -r requirements.txt
```

## Directories

The code will run assuming particular folders exist. Run the following block of code in your command line to ensure they are all there

```bash
cd Working Directory

mkdir corpora
mkdir corpora/zenodo
mkdir copora/extraced-tweets
mkdir corpora/cleaned-tweets
mkdir corpora/csw

mkdir dictionaries
mkdir dictionaries/dict.cc
mkdir dictionaries/dict_leipzig
mkdir dictionaries/urban-dictionary
```

## Dataset

The entire dataset used is available for non-commercial download from [here](https://zenodo.org/record/6624514). Each zip file should be un-zipped into the zenodo dictionary made above.

## Dictionaries

### The following dictionaries should be downloaded:

1. Leipzig dictionaries were downloaded into the dict-leipzig directory from [here](https://wortschatz.uni-leipzig.de/en/download):

   - 100k English News 2020
   - 300k German News 2021
   - 100k Austrian News 2012
   - 300k Swiss News 2012

2. Large German Dictionary was downloaded into the dict.cc dictionary from [dict.cc](dict.cc) from [here](https://www1.dict.cc/translation_file_request.php?l=e)

3. Urban dictionary was taken from the GitHub page [here]() into a directory in urban-dictionary with a file for each first word character

## Preprocessing
Extract and clean the tweets first

```angular2html
python3 src/preprocessing.py
```

## Dictionary compilation
Compile the relevant dictionaries and combine into a 'Code-switching' dictionary

```angular2html
python3 src/dictionaries.py
```

## Code-switched tweet detection
Use the dictionary and cleaned tweets to identify tweets that use Code-switching, saving them into the copora/csw directory

```angular2html
python3 src/csw.py
```

## Citations Counter

A method was implemented to count Code-switching related citations from ACL, as contained in the acl-citations.py script and depicted in the report.

## Contact

Please do drop me an email at is473@cam.ac.uk with any questions for about this project
