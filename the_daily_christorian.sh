#!/bin/bash
FOLDER=/tmp/cwcki_source
MONTH=$(LC_ALL=C date +%B)
YEAR=$(LC_ALL=C date +%Y)

rm -rf $FOLDER
mkdir $FOLDER
wget https://sonichu.com/cwcki -P $FOLDER
wget https://sonichu.com/cwcki/"$MONTH"_"$YEAR"_social_media_posts -P $FOLDER
python3 the_daily_christorian.py
