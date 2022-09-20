#!/bin/sh

INPUT='../ex00/hh.json'

OUTPUT='hh.csv'

FILTER='filter.jq'

jq -r -f $FILTER $INPUT > $OUTPUT