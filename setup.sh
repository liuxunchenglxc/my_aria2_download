DEBIAN_FRONTEND=noninteractive apt update \
&& apt install -y \
aria2 \
&& rm -rf /var/lib/apt/lists/*