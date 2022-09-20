#!/bin/sh 

INPUT='../ex03/hh_positions.csv'

DIR="created"
mkdir -p $DIR

PREFIX="created_at_"
EXTENTION=".csv"

DATE=$(cat $INPUT | tail -n +2 \
| awk 'BEGIN{FS=",\""} 
{
    split($2, result, "T");
    print result[1];
}' \
| sort \
| uniq \
)

for date in $DATE
do FILE="$DIR/$PREFIX$date$EXTENTION"
touch $FILE

cat $INPUT | head -n 1 > $FILE

cat $INPUT | tail -n +2 \
| awk -v date=$date \
    'BEGIN {FS=OFS=","}
    {
        i = index($2, date);
        if (i > 0)
        {
            print $0;
        }
    }' >> $FILE
done