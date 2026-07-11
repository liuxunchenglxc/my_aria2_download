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
    ## {
    ##     "url": "https://www.youtube.com/watch?v=qMDJH78tn0I",
    ##     "filename": "qMDJH78tn0I.mkv",
    ##     "note": "《玄学大佬回京：一卦算哭满朝文武2》第1~81集",
    ##     "type": "ytdlp"
    ## },
    # {
    #     "url": "https://www.youtube.com/watch?v=Zq1B1qdF_Cg",
    #     "filename": "Zq1B1qdFCg.mkv",
    #     "note": "《玄学大佬回京：一卦算哭满朝文武》第3季",
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
    ## {
    ##     "url": "https://www.youtube.com/watch?v=jG1O_nQIDOU",
    ##     "filename": "jG1OnQIDOU.mkv",
    ##     "note": "《全宗起飞之大佬到宗门当弟子》第1~54集",
    ##     "type": "ytdlp"
    ## },
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
    ## {
    ##     "url": "https://www.youtube.com/watch?v=-JMVT7fRsR4",
    ##     "filename": "JMVT7fRsR4.mkv",
    ##     "note": "《苟道修仙记》第1~79集",
    ##     "type": "ytdlp"
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
    ## {
    ##     "url": "https://www.youtube.com/watch?v=wTplLSQtVw4",
    ##     "filename": "wTplLSQtVw4.mkv",
    ##     "note": "《开局大帝：我的弟子全是逆天体质》第1~134集",
    ##     "type": "ytdlp"
    ## },
    ## {
    ##     "url": "https://www.youtube.com/watch?v=jkVyXJqGfmk",
    ##     "filename": "jkVyXJqGfmk.mkv",
    ##     "note": "《开局大帝：我的弟子全是逆天体质》第2季",
    ##     "type": "ytdlp"
    ## },
    # {
    #     "url": "https://www.youtube.com/watch?v=IUkwVSqtVmQ",
    #     "filename": "IUkwVSqtVmQ.mkv",
    #     "note": "《开局大帝：我的弟子全是逆天体质》第3季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=dCZ6SaCEf9s",
    #     "filename": "dCZ6SaCEf9s.mkv",
    #     "note": "《带着别墅穿大唐第一季》第1~3集",
    #     "type": "ytdlp"
    # },
    ## {
    ##     "url": "https://www.youtube.com/watch?v=okC7kh-apQ4",
    ##     "filename": "okC7khapQ4.mkv",
    ##     "note": "《仙眼》第1~127集",
    ##     "type": "ytdlp"
    ## },
    # {
    #     "url": "https://www.youtube.com/watch?v=R529MdZsYbk",
    #     "filename": "R529MdZsYbk.mkv",
    #     "note": "《仙眼》第2季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=mpPAcCy2SdM",
    #     "filename": "mpPAcCy2SdM.mkv",
    #     "note": "《在修仙界收废品的我，悄悄无敌了》第1~138集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=sbfcydxwdkE",
    #     "filename": "sbfcydxwdkE.mkv",
    #     "note": "《罪妻发配边关，罪妻开荒养出战神》第1~7季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=DwmQrNjdJ5g",
    #     "filename": "DwmQrNjdJ5g.mkv",
    #     "note": "《风落西疆，从官门贵女到荒原寨主》第1~95集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=_Uf-2ZbdOso",
    #     "filename": "Uf2ZbdOso.mkv",
    #     "note": "《什么召唤系，我不是在请神吗？》第1~76集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=WV_LUf8-Qr0",
    #     "filename": "WVLUf8Qr0.mkv",
    #     "note": "《戒指通现代，古代海鲜卖爆了》第1~113集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=7xxm-QUDVGM",
    #     "filename": "7xxmQUDVGM.mkv",
    #     "note": "《凡人弑仙传》第1~97集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=ik3etQSH7uM",
    #     "filename": "ik3etQSH7uM.mkv",
    #     "note": "《少年生来不信命，横刀立马轻王侯3d版》",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=XwbGNGWnCVM",
    #     "filename": "XwbGNGWnCVM.mkv",
    #     "note": "《万妖图录传》第1~6季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=tLKqv78AxSc",
    #     "filename": "tLKqv78AxSc.mkv",
    #     "note": "《万妖图录传》第7季",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=ATHk2s4MHk0",
    #     "filename": "ATHk2s4MHk0.mkv",
    #     "note": "《万妖图录之寒玉优昙(第八季）》",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://d34w7g4gy10iej.cloudfront.net/release_03/uap_videos_061226.zip",
    #     "filename": "ufo_release_03_videos.zip",
    #     "note": "ufo_release_03",
    #     "type": "aria2"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=JhA2Kg0LtoE",
    #     "filename": "JhA2Kg0LtoE.mkv",
    #     "note": "《赠物得长生，老头修仙记！》第1~114集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=N0z13S1ivcI",
    #     "filename": "N0z13S1ivcI.mkv",
    #     "note": "《遮天剑神》完整版",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=uf8Op_N9Qj0",
    #     "filename": "uf8OpN9Qj0.mkv",
    #     "note": "【超爽看过瘾】《仙武传》第1~267集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=PO8gvmsbDrM",
    #     "filename": "PO8gvmsbDrM.mkv",
    #     "note": "一代天才玄脉受损成为废物，新婚之夜遭人毒害。玄天至宝，轮回镜现，逆天改命，带着仇恨与遗憾，誓要登顶力量的巅峰！",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=rAdYl0aHM-k",
    #     "filename": "rAdYl0aHMk.mkv",
    #     "note": "《今昭北猎之长姐逆袭》",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=7mq5YrvawyI",
    #     "filename": "7mq5YrvawyI.mkv",
    #     "note": "《独守镖宅：携哑妹度荒年》第1~97集",
    #     "type": "ytdlp"
    # },
    # {
    #     "url": "https://www.youtube.com/watch?v=Rqcubm46owk",
    #     "filename": "Rqcubm46owk.mkv",
    #     "note": "《我家娘子惹不起》",
    #     "type": "ytdlp"
    # },
    {
        "url": "https://www.youtube.com/watch?v=a0u75CgXM8w",
        "filename": "a0u75CgXM8w.mkv",
        "note": "《帅府福崽2福星奶团来旺家，帅府全家宠不停》",
        "type": "ytdlp"
    },
    {
        "url": "https://www.youtube.com/watch?v=Yoi4bk9yRCk",
        "filename": "Yoi4bk9yRCk.mkv",
        "note": "《我捡了个阿姐，她带我家逆天改命》",
        "type": "ytdlp"
    },
    {
        "url": "https://www.youtube.com/watch?v=qbyEeolMKDk",
        "filename": "qbyEeolMKDk.mkv",
        "note": "《山海经之万兽图鉴》",
        "type": "ytdlp"
    },
    {
        "url": "https://www.youtube.com/watch?v=-5ZK79SGDNE",
        "filename": "5ZK79SGDNE.mkv",
        "note": "《陆家新妇不好惹》",
        "type": "ytdlp"
    },
    {
        "url": "https://www.youtube.com/watch?v=oh7YflZN3ow",
        "filename": "oh7YflZN3ow.mkv",
        "note": "《遇强则强，仙帝来了也得跪下！》",
        "type": "ytdlp"
    },
]

# download_list = [
#     {
#         "url": "https://www.youtube.com/watch?v=Rm5jpqnpX8Y",
#         "filename": "Rm5jpqnpX8Y.mkv",
#         "note": "《我这个反派强得离谱》第1~93集",
#         "type": "ytdlp"
#     },
#     {
#         "url": "https://www.youtube.com/watch?v=LulKGQrEoPU",
#         "filename": "LulKGQrEoPU.mkv",
#         "note": "《天命反派：女帝姐姐别追了》第1~94集",
#         "type": "ytdlp"
#     },
#   {
#         "url": "https://www.youtube.com/watch?v=0Aj6Iq6g1mQ",
#         "filename": "0Aj6Iq6g1mQ.mkv",
#         "note": "《拾光小丫》第1~122集",
#         "type": "ytdlp"
#     },
# ]

# download_list = [
#     {
#         "url": "https://www.youtube.com/watch?v=8o8c_Htrt_E",
#         "filename": "8o8cHtrtE.mkv",
#         "note": "《穿成炮灰后：不是反派吗？怎么要抱抱》第1~68集",
#         "type": "ytdlp"
#     },
#     {
#         "url": "https://www.youtube.com/watch?v=Ap7zZddKq-A",
#         "filename": "Ap7zZddKqA.mkv",
#         "note": "《穿成炮灰后：不是反派吗？怎么要抱抱》第2季",
#         "type": "ytdlp"
#     },
#     {
#         "url": "https://www.youtube.com/watch?v=1xBtN_buuls",
#         "filename": "1xBtNbuuls.mkv",
#         "note": "《穿成炮灰后：不是反派吗？怎么要抱抱》第3季",
#         "type": "ytdlp"
#     },
#     {
#         "url": "https://www.youtube.com/watch?v=TVj3FWxKgso",
#         "filename": "TVj3FWxKgso.mkv",
#         "note": "《穿成炮灰后：不是反派吗？怎么要抱抱》第4季",
#         "type": "ytdlp"
#     },
# ]

# download_list = [
#     {
#         "url": "https://www.youtube.com/watch?v=TKI9HNZt6U0",
#         "filename": "TKI9HNZt6U0.mkv",
#         "note": "《日行一善，女帝惊呼反派竟成圣人了》第1~2季",
#         "type": "ytdlp"
#     },
#     {
#         "url": "https://www.youtube.com/watch?v=aCxRRFHAyuA",
#         "filename": "aCxRRFHAyuA.mkv",
#         "note": "《日行一善，女帝惊呼反派竟成圣人了》第3季",
#         "type": "ytdlp"
#     },
# ]

download_list = [
    {
        "url": "https://d34w7g4gy10iej.cloudfront.net/release_04/uap_release04_videos_071026.zip",
        "filename": "uap_release04_videos_071026.zip",
        "note": "UAP第四次公开视频",
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
