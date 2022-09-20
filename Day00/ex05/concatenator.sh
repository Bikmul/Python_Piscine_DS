#!/bin/sh

DIR="created"
PREFIX="created_at_"
EXTENSION="csv"

OUTPUT="./hh_positions.csv"

LIST=($(ls $DIR/$PREFIX*$EXTENTION))


cat ${LIST[0]} | head -n 1 > $OUTPUT

for file in ${LIST[@]}
do
  cat $file | tail -n +2 >> $OUTPUT
done
