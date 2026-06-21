url=$1
name=$2

echo "start yt-dlp_linux"
echo "url="$1
echo "name="$2

yt-dlp_linux \
  --cookies cookies.txt \
  -N 4 \
  --impersonate chrome \
  --write-subs \
  --write-auto-subs \
  --sub-langs "zh.*,en.*" \
  --embed-thumbnail \
  --embed-metadata \
  --audio-quality 0 \
  --merge-output-format mkv \
  -o "$name" \
  "$url"