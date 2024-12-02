#!/bin/bash

numDay=$(date +'%-d')

echo "Creating the setup for day $numDay"

if [ ! -d "day$numDay" ]
then
  mkdir "day$numDay"
else
    echo "Directory yday$numDay already exists. Exiting..."
    exit 0
fi

cd "day$numDay"

touch advent.py && touch input.txt && touch example.txt

curl -o input.txt -b session=$(cat ../.aocrc) -H "User-Agent: pekka-1992@hotmail.com" https://adventofcode.com/2024/day/$numDay/input

echo "Setup done!"