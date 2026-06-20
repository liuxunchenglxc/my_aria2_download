name=$1
note=$2
bzid=$3
curl -#o - -T -H "Authorization: Bearer "$bzid $name "https://w.buzzheavier.com/p348490rwt76/"$name'?note=$(echo -n "'$note'" | base64)"' | cat