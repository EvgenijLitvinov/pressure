#!/bin/bash

read -p "Комментарий для коммита: "
echo ${REPLY} > flag.txt
git commit -a -F flag.txt
git push
curl -T flag.txt ftp://y95891gg:Vf4pra2a@y95891gg.beget.tech/y95891gg.beget.tech/public_html/pressure/
