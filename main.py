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
    # {
    #     "url": "https://www.youtube.com/watch?v=-JMVT7fRsR4",
    #     "filename": "JMVT7fRsR4.mkv",
    #     "note": "《苟道修仙记》第1~79集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=CKovPtf-di4",
    #     "filename": "CKovPtfdi4.mkv",
    #     "note": "《苟道修仙记》第2季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=C2U0aseHIpk",
    #     "filename": "C2U0aseHIpk.mkv",
    #     "note": "《穿越60年代，觉醒超市系统》第1~92集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=VHHRzbhzqS8",
    #     "filename": "VHHRzbhzqS8.mkv",
    #     "note": "《我家后墙通边关》第1~76集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=QEFLi2J2Rtw",
    #     "filename": "QEFLi2J2Rtw.mkv",
    #     "note": "《异世雇工之山庄通异界古人来打工》第1~80集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=wTplLSQtVw4",
    #     "filename": "wTplLSQtVw4.mkv",
    #     "note": "《开局大帝：我的弟子全是逆天体质》第1~134集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=jkVyXJqGfmk",
    #     "filename": "jkVyXJqGfmk.mkv",
    #     "note": "《开局大帝：我的弟子全是逆天体质》第2季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://d34w7g4gy10iej.cloudfront.net/release_03/uap_videos_061226.zip",
    #     "filename": "ufo_release_03_videos.zip",
    #     "note": "ufo_release_03",
    #     "type": "aria2"
    # },
    {
        "url": r"https://abra--5e4bd524.api.cosmic-crab.buzz/f5c2c71aa5e65c406e44a9a41157d1951e25e791/Major%20Ed%20Dames%20-%20Remote%20Viewing%20%284-Disc%29~arch/Major%20Ed%20Dames%20-%20Remote%20Viewing%20%284-Disc%29.zip?api-key=8acbcf1e-732c-4574-a3bf-27e6a85b86f1&download=true&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODI4MjIwMDUsInJhdGUiOiI1TSIsInJvbGUiOiJmcmVlIiwic2Vzc2lvbklEIjoiTVRjNE1qY3pOVFUzT0h4T2QzZEJUa1prVVU1cVRYcFhSVkpMVjFWU1NsZEdRbGxXUkVwQ1VqRkJNbE5FWkVsVVJGVXhVMVJPUlZKVlVsTlNha3BGVTFWc1ZGVkZSa0pOYkVKSlZrVTFTMDFyVGs5WFZVVTlmRW1PV013OTRmdjFpcnJ0V0l3WXFxZC1GYlRGeHNGY2tMM0pqVEo2SUxubCIsImRvbWFpbiI6IndlYnRvci5pbyIsImFnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTQwLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTQwLjAiLCJyZW1vdGVBZGRyZXNzIjoiMTA0LjI4LjIxNS42NyJ9.hdh4COPFYDZ6bLqp4AbUVrpUoJcC3XT7jZiOD18laVY",
        "filename": r"Major%20Ed%20Dames%20-%20Remote%20Viewing%20%284-Disc%29.zip",
        "note": "MajorEdDamesRemoteViewing",
        "type": "aria2"
    },
]

def upload(item):
    url = f'https://w.buzzheavier.com/p348490rwt76/{item["filename"]}'#?note={base64.b64encode(item["note"].encode("utf-8")).decode("utf-8")}'
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
