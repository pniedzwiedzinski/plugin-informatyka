#!/bin/sh

set -x
set -ueo pipefail

cd /app/informatyka
git --git-dir=/app/git status | grep $(/app/re_pattern.py | sed "s=|=\\\|=g") | zip $(/app/get_filename.py) $(cat)
mv "$(/app/get_filename.py).zip" /app
cd /app
python3 main.py
cd /app/informatyka
git --git-dir=/app/git add .
git --git-dir=/app/git commit -m "Informatyka - dodano automatycznie"
git --git-dir=/app/git push