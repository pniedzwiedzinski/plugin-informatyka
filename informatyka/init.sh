#!/bin/sh

set -x
set -ueo pipefail

cd /app/informatyka
mkdir /app/git
git --git-dir=/app/git init
echo "Succesfully initialized directory"