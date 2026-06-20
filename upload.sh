name=$1
url=$2
bzid=$3
curl -#o - -T -H $bzid $name $url | cat