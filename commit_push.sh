#!/bin/bash

read -p "Комментарий для коммита: "
git commit -a -m $REPLY
#git push
#echo "1" > ../pressure/flag.txt
