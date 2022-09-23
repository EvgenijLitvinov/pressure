#!/bin/bash

read -p "Комментарий для коммита: "
echo ${REPLY} > asd.txt
git commit -a -F asd.txt
#git push
#echo "1" > ../pressure/flag.txt
echo \'${REPLY}\'
