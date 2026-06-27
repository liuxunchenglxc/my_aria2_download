import subprocess
import argparse
import base64
from get_cook import download_cook
import os

parser = argparse.ArgumentParser(description="")
parser.add_argument("--BUZZHEAVIER_ID", required=True, help="BUZZHEAVIER_ID")

args = parser.parse_args()

############################

# setup
subprocess.run(["bash", "setup.sh"], text=True)
download_cook(args.BUZZHEAVIER_ID)

#############################

# download
download_list = [
    # {
    #     "url": "https://www.youtube.com/watch?v=6AmcRMj3AM0",
    #     "filename": "CRo8QkXVDvA.mkv",
    #     "note": "《开局一条蛇，我无限进化》第1~83集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=qMDJH78tn0I",
    #     "filename": "qMDJH78tn0I.mkv",
    #     "note": "《玄学大佬回京：一卦算哭满朝文武2》第1~81集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=KacjAmJmgc4",
    #     "filename": "KacjAmJmgc4.mkv",
    #     "note": "《从死囚营崛起》第1~3季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=m1E2MFifqJI",
    #     "filename": "m1E2MFifqJI.mkv",
    #     "note": "《穿成恋爱脑村姑，被祸害的全家有救了》第1~80集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=4b3DCaeMJhE",
    #     "filename": "4b3DCaeMJhE.mkv",
    #     "note": "《末日天灾：我用空间囤了百亿物资》第1~100集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=jG1O_nQIDOU",
    #     "filename": "jG1OnQIDOU.mkv",
    #     "note": "《全宗起飞之大佬到宗门当弟子》第1~54集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=kYuWmQrcN5U",
    #     "filename": "kYuWmQrcN5U.mkv",
    #     "note": "《全宗起飞之大佬到宗门当弟子》第2季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=qYavIGqk_Ds",
    #     "filename": "qYavIGqkDs.mkv",
    #     "note": "《超市通异界，我在修真各界搞倒卖》第1~77集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=UnxoZC4-zRE",
    #     "filename": "UnxoZC4zRE.mkv",
    #     "note": "《普通弓箭手？我能无限叠加攻击力》第1~60集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=MWjQCaaJTxA",
    #     "filename": "MWjQCaaJTxA.mkv",
    #     "note": "《血量亿倍增幅，被当成废物异能》第1~77集",
    #     "type": "ytdlp"
    # },
    {
        "url": "https://www.youtube.com/watch?v=-JMVT7fRsR4",
        "filename": "JMVT7fRsR4.mkv",
        "note": "《苟道修仙记》第1~79集",
        "type": "ytdlp"
    },
    {
        "url": "https://www.youtube.com/watch?v=CKovPtf-di4",
        "filename": "CKovPtfdi4.mkv",
        "note": "《苟道修仙记》第2季",
        "type": "ytdlp"
    },
    # {
    #     "url": "https://d34w7g4gy10iej.cloudfront.net/release_03/uap_videos_061226.zip",
    #     "filename": "ufo_release_03_videos.zip",
    #     "note": "ufo_release_03",
    #     "type": "aria2"
    # },
]

def upload(item):
    url = f'https://w.buzzheavier.com/p348490rwt76/{item["filename"]}?note={base64.b64encode(item["note"].encode("utf-8")).decode("utf-8")}'
    bzid = f"Authorization: Bearer {args.BUZZHEAVIER_ID}"
    subprocess.run(["bash", "upload.sh", item["filename"], url, bzid], text=True)
    # 删除上传过的文件
    try:
        os.remove(item["filename"])
    except:
        pass

for item in download_list:
    if item["type"] == "aria2":
        subprocess.run(["bash", "aria2_download.sh", item["url"], item["filename"]], text=True)
    elif item["type"] == "ytdlp":
        subprocess.run(["bash", "ytdlp_download.sh", item["url"], item["filename"]], text=True)
    upload(item)

####################
