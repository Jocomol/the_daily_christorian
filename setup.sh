#!/bin/bash
mkdir daily_chris_chan
if ! command -v pip3 &> /dev/null
then
	echo "pip3 isn't installed"
	exit
fi
pip3 install -r requirements.txt
