from encodings.base64_codec import base64_encode
import subprocess
import argparse
import base64

parser = argparse.ArgumentParser(description="")
parser.add_argument("--BUZZHEAVIER_ID", required=True, help="BUZZHEAVIER_ID")

args = parser.parse_args()

# setup
# subprocess.run("bash setup.sh", shell=True, text=True)

# download
download_list = [
    {
        "url": "https://www.war.gov/medialink/ufo/061226/release_03/release_03_documents.zip",
        "filename": "ufo_release_03_documents.zip",
        "note": "美国战争部UFO第三批公开文档",
    },
    {
        "url": "https://d34w7g4gy10iej.cloudfront.net/release_03/uap_videos_061226.zip",
        "filename": "ufo_release_03_videos.zip",
        "note": "美国战争部UFO第三批公开视频",
    },
]

for item in download_list:
    subprocess.run(f"bash download.sh {item["url"]} {item["filename"]}", shell=True, text=True)

# upload
for item in download_list:
    url = f'https://w.buzzheavier.com/p348490rwt76/{item["filename"]}?note={base64.b64encode(item["note"].encode("utf-8")).decode("utf-8")}'
    subprocess.run(f"bash upload.sh {item["filename"]} {url} {args.BUZZHEAVIER_ID}", shell=True, text=True)