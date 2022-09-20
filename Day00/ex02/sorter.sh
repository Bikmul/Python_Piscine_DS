#!/bin/sh

INPUT='../ex01/hh.csv'

OUTPUT='hh_sorted.csv'

cat $INPUT | head -n 1 > $OUTPUT

cat $INPUT | tail -n +2 | sort --field-separator=',' --key=2,2 --key=1,1 >> $OUTPUT