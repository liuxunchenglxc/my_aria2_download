name=$1
url=$2
bzid=$3
curl -#o - -X PUT -T -H $bzid $name $url | cat