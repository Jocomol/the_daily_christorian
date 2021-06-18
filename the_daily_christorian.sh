#!/bin/bash
FOLDER=/tmp/cwcki_source
MONTH=$(LC_ALL=C date +%B)
YEAR=$(LC_ALL=C date +%Y)
DATE=$(LC_ALL=C date +%d)
POSTS=daily_chris_chan
FILE=$POSTS/$YEAR-$MONTH-$DATE-post.html

rm -rf $FOLDER
mkdir $FOLDER
wget https://sonichu.com/cwcki -P $FOLDER
wget https://sonichu.com/cwcki/"$MONTH"_"$YEAR"_social_media_posts -P $FOLDER
cp template.html $FILE
python3 the_daily_christorian.py $FILE
./sup $FILE
