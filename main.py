import subprocess
import argparse
import base64
from get_cook import download_cook

parser = argparse.ArgumentParser(description="")
parser.add_argument("--BUZZHEAVIER_ID", required=True, help="BUZZHEAVIER_ID")

args = parser.parse_args()

############################

# setup
download_cook(args.BUZZHEAVIER_ID)
# subprocess.run("bash setup.sh", shell=True, text=True)

#############################

# download
download_list = [
    {
        "url": "https://www.youtube.com/watch?v=CRo8QkXVDvA&pp=0gcJCT8LAYcqIYzv",
        "filename": "CRo8QkXVDvA.mkv",
        "note": "《玄幻：开局一条蛇，我无限进化》第1~64集",
        "type": "ytdlp"
    },
    # {
    #     "url": "https://d34w7g4gy10iej.cloudfront.net/release_03/uap_videos_061226.zip",
    #     "filename": "ufo_release_03_videos.zip",
    #     "note": "ufo_release_03",
    #     "type": "aria2"
    # },
]

for item in download_list:
    if item["type"] == "aria2":
        subprocess.run(["bash", "aria2_download.sh", item["url"], item["filename"]], text=True)
    elif item["type"] == "ytdlp":
        subprocess.run(["bash", "ytdlp_download.sh", item["url"], item["filename"]], text=True)

####################

# upload
for item in download_list:
    url = f'https://w.buzzheavier.com/p348490rwt76/{item["filename"]}?note={base64.b64encode(item["note"].encode("utf-8")).decode("utf-8")}'
    bzid = f"Authorization: Bearer {args.BUZZHEAVIER_ID}"
    subprocess.run(["bash", "upload.sh", item["filename"], url, bzid], text=True)