#!/bin/bash

read -e -p "Комментарий для коммита: " COMENT
git commit -a -m '$COMENT'
git push
#echo "1" > ../pressure/flag.txt
