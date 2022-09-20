#!/bin/sh

OUTPUT="./hh.json"
COUNT="20"

NAME="${1/ /+}"

curl -K -H 'User-Agent: api-test-agent' -G "https://api.hh.ru/vacancies?text=$NAME&per_page=$COUNT" | jq > $OUTPUT
