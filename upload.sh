name=$1
url=$2
bzid=$3
curl -#o - -X PUT -H $bzid -T $name $url | cat