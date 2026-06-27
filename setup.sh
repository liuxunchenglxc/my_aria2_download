yt-dlp_linux --update-to nightly

echo "yt-dlp_linux --update-to nightly ok!"

ORG_NAME=Brainicism
REPO_NAME=bgutil-ytdlp-pot-provider
LATEST_VERSION=$(curl -s https://api.github.com/repos/${ORG_NAME}/${REPO_NAME}/releases | grep -m 1 "tag_name" | cut -d'"' -f4)

FILE_NAME=bgutil-ytdlp-pot-provider.zip 

echo "${ORG_NAME}/${REPO_NAME} 最新版本是: ${LATEST_VERSION}"
mkdir -p ~/yt-dlp-plugins
curl -L "https://github.com/${ORG_NAME}/${REPO_NAME}/releases/download/${LATEST_VERSION}/${FILE_NAME}" -o ~/yt-dlp-plugins/${FILE_NAME}

echo "${FILE_NAME} ok!"