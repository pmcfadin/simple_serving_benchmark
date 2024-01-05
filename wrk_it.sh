#!/bin/bash

URL=${1//\//_}
OUTPUT_FILE="test_output/output_${URL}.json"

cassowary run -u http://localhost:8080/ -c 10 -n 1000000 --json-metrics --json-metrics-file=$OUTPUT_FILE
