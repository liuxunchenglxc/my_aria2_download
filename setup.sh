yt-dlp_linux --update-to nightly

echo "yt-dlp_linux --update-to nightly ok!"

ORG_NAME=Brainicism
REPO_NAME=bgutil-ytdlp-pot-provider
LATEST_VERSION=$(curl -s https://api.github.com/repos/${ORG_NAME}/${REPO_NAME}/releases | grep -m 1 "tag_name" | cut -d'"' -f4)

# FILE_NAME=bgutil-ytdlp-pot-provider.zip

# echo "${ORG_NAME}/${REPO_NAME} 最新版本是: ${LATEST_VERSION}"
# mkdir -p ~/yt-dlp-plugins
# curl -L "https://github.com/${ORG_NAME}/${REPO_NAME}/releases/download/${LATEST_VERSION}/${FILE_NAME}" -o ~/yt-dlp-plugins/${FILE_NAME}

# echo "${FILE_NAME} ok!"

if [ "$LATEST_VERSION" == "$YT_POT_VERSION" ]; then
   echo "Brainicism/bgutil-ytdlp-pot-provider版本最新"
else
   echo "有新版本Brainicism/bgutil-ytdlp-pot-provider可用！当前版本: $YT_POT_VERSION，最新版本: $LATEST_VERSION"
   echo "https://github.com/Brainicism/bgutil-ytdlp-pot-provider"
   curl -s -X POST "https://api.telegram.org/${{ secrets.TG_TOKEN }}/sendMessage" \
        -d "chat_id=${{ secrets.TG_CHAT_ID }}" \
        -d "text=⚠️ 插件有新版本了！%0A当前版本: $YT_POT_VERSION%0A最新版本: $LATEST_VERSION"
fi