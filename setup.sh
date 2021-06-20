#!/bin/bash
WEBFOLDER=/var/www/html/thedailychristorian

mkdir $WEBFOLDER
mkdir $WEBFOLDER/daily_chris_chan
cp index.html $WEBFOLDER
cp sup $WEBFOLDER
cp the_daily_christorian.* $WEBFOLDER
cp $WEBFOLDER/templates/rss.xml $WEBFOLDER
mkdir $WEBFOLDER/daily_chris_chan

if ! command -v pip3 &> /dev/null
then
	echo "pip3 isn't installed"
	exit
fi
pip3 install -r requirements.txt
