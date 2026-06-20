url=$1
name=$2
aria2c --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0" -c -s 16 -x 16 -k 1M $url -o $name