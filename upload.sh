name=$1
url=$2
bzid=$3
# echo curl -#o - -X PUT -T "$name" -H "$bzid" $url | cat
curl -#o - -X PUT -T "$name" -H "$bzid" $url | cat