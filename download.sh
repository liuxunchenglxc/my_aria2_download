url=$1
name=$2
aria2c -c -s 16 -x 16 -k 1M $url -o $name