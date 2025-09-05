#!/bin/bash

repo="$1"

git remote add "$repo" https://aur.archlinux.org/"$repo".git
git fetch "$repo"
git checkout -b "$repo" "$repo"/master
git checkout main
git push -u origin --all