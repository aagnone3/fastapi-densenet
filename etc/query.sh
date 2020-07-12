#!/usr/bin/env bash
set -eou pipefail
source ./env

server=localhost:$SERVER_PORT
query_file=/tmp/query.json

path=${1?Please pass a local path to a text snippet to analyze.}
echo "{\"text\": \"$path\"}" | sed 's/\\//g' > $query_file

curl \
    -X POST \
    $server/sentiment \
    -d @$query_file \
    2>/dev/null
rm -f $query_file