import pytube
import json
import os
import sys
import requests


BASE_DIR = "/run/media/coderdude/Adwait/Study/Other Institutions/MIT/6.824 _Distributed_Systems/"
JSON_FILE = "./course_material.json"


if __name__ == "__main__":
    all_classes = json.loads(open(JSON_FILE).read())
    skip_flag = True #to skip till lec 13
    for cl in all_classes:
        if cl["class_name"] == "LEC 21":
            skip_flag = False
        
        if(skip_flag):
            continue
        
        if cl["type"] != "lec":
            continue

        dir_path = os.path.join(BASE_DIR, cl["class_name"])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        print(f"Downloading Videos for {cl['class_name']}")
        for vidlink in cl["ytvideos"]:
            try:
                yt = pytube.YouTube(vidlink)
            except:
                print(f"ConnError for link {vidlink}. Error: {sys.exc_info()[0]}")
                continue

            video = yt.streams.get_highest_resolution()
            video.download(dir_path)
            print(f"video downloaded for class {cl['class_name']} link: {vidlink}")

        # for key in cl:
        #     if key in ["class_name", "type"]:
        #         continue

        #     for lk in cl[key]:
        #         if lk.endswith("txt") or lk.endswith("pdf") :
        #             last_entry = lk.split("/")[-1]
        #             req = requests.get(lk, allow_redirects = True)
        #             with open(f"{dir_path}/{key}__{last_entry}", "wb") as content_file:
        #                 content_file.write(req.content)
                    
        #             print(f"Downloaded {lk} at {dir_path}")

        
        

