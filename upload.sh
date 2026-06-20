name=$1
url=$2
bzid=$3
curl -#o - -H $bzid -T $name $url | cat