#!/bin/sh

INPUT='../ex03/hh_positions.csv'

OUTPUT='hh_uniq_positions.csv'

echo '"name","count"' > $OUTPUT
J=`grep "Junior" $INPUT | wc -l`
M=`grep "Middle" $INPUT | wc -l`
S=`grep "Senior" $INPUT | wc -l`
echo "\"Junior\",$J" | sed 's/ //g' >> $OUTPUT
echo "\"Middle\",$M" | sed 's/ //g' >> $OUTPUT
echo "\"Senior\",$S" | sed 's/ //g' >> $OUTPUT