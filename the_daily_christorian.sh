#!/bin/bash
FOLDER=/tmp/cwcki_source
MONTH=$(LC_ALL=C date +%B)
YEAR=$(LC_ALL=C date +%Y)
DATE=$(LC_ALL=C date +%d)
POSTS=daily_chris_chan
FULLPATH=$(dirname $0)
FILE=$FULLPATH/$POSTS/$YEAR-$MONTH-$DATE-post.html

rm -rf $FOLDER
mkdir $FOLDER
wget https://sonichu.com/cwcki -P $FOLDER
#wget https://sonichu.com/cwcki/"$MONTH"_"$YEAR"_social_media_posts -P $FOLDER #Chris is in prison and doesn't post anything
touch $FILE
python3 the_daily_christorian.py > $FILE 
./sup $FILE
