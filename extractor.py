import os
import json

RECORDINGS_DIR = "corpora/zenodo-tweets/german-tweet-sample-2022-04/"
date = RECORDINGS_DIR[-8:-1]

with open(f"corpora/extracted-tweets/all-tweets-{date}.txt", 'w', encoding='utf-8') as w:
    for count, recording in enumerate(os.listdir(RECORDINGS_DIR)):
        recording += '/'
        json_file = os.listdir(RECORDINGS_DIR + recording)[0]

        with open(RECORDINGS_DIR + recording + json_file) as f:
            data = json.load(f)

        print(f"Writing text for {len(data)} tweets in file number {count+1}/{len(os.listdir(RECORDINGS_DIR))}")
        i = 0
        for tweet in data:
            if "text" in tweet:
                i += 1
                tweet = tweet["text"].replace("\n", " ")
                w.write(tweet)
                w.write(" \n")
        print(f"Done file and outputted {i} text tweets.")