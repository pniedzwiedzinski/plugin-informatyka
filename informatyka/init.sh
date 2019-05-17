#!/bin/sh

set -ueo pipefail

cd /app/informatyka

git rev-parse --git-dir

if [[ $? -eq 0 ]]; then
    echo "Already initialized."
    exit
fi

set -x
mkdir /app/git

git --git-dir=/app/git init
echo "Succesfully initialized directory"