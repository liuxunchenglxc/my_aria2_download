name=$1
url=$2
bzid=$3
curl -#o - -T -H "Authorization: Bearer "$bzid $name $url | cat