#!/usr/bin/env sh

set -e

npm run build

cd dist

git init
git add -A
git commit -m 'New deploy'
git push -f git@github.com:JorgeJFCovello/super-duper-conquer full_front_branch:github_pages_deploy
cd -