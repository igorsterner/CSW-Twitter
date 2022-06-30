import os
import json

RECORDINGS_DIR = r"corpora/zenodo-tweets/german-tweet-sample-2022-01/"
date = RECORDINGS_DIR[-8:-1]
EXTRACTED_DIR = f"corpora/extracted-tweets/all-tweets-{date}-test.txt"

with open(EXTRACTED_DIR, 'w', encoding='utf-8') as w:
    for count, recording in enumerate(os.listdir(RECORDINGS_DIR)):

        RECORDING_DIR = os.path.join(RECORDINGS_DIR, recording)
        json_file = os.listdir(RECORDING_DIR)[0]
        JSON_DIR = os.path.join(RECORDING_DIR, json_file)

        with open(JSON_DIR) as f:
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