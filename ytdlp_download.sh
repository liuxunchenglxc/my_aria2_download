url=$1
name=$2

echo "start yt-dlp_linux"
echo "url="$1
echo "name="$2

yt-dlp_linux -v \
  --extractor-args "youtube:player_client=mweb,web_music,web_embedded,tv,web_creator,web_safari,web;youtubepot-bgutilscript:server_home=bgutil-ytdlp-pot-provider/server" \
  --cookies cookies.txt \
  -N 4 \
  --impersonate chrome \
  --write-subs \
  --write-auto-subs \
  --sub-langs "zh-[a-zA-Z]+,en" \
  --embed-thumbnail \
  --embed-metadata \
  --embed-subs \
  --embed-chapters \
  --embed-info-json \
  --audio-quality 0 \
  --merge-output-format mkv \
  -o "$name" \
  "$url"