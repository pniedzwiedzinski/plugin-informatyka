#!/bin/sh

set -x
set -ueo pipefail

cd /app/informatyka
git status -u | grep .cpp | zip inf $(cat)
mv inf.zip /app
cd /app
python3 main.py
cd /app/informatyka
git add .
git commit -m "Informatyka - dodano automatycznie"
git push