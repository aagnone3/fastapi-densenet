#!/usr/bin/env bash
set -eou pipefail
source ./env

server=${1}
shift 1
query=$(echo "{\"text\": \"$@\"}" | sed 's/\\//g')

curl \
    -X POST \
    $server \
    -d "$query" \
    2>/dev/null

[[ $? -eq 0 ]] || {
    echo "Error performing query"
    exit 1
}
echo