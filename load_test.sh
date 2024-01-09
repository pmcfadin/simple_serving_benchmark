#!/bin/bash

TEST=${1//\//_}
OUTPUT_FILE="test_output/output_${TEST}.json"

# Python version needed to run cassowary without timeout failures
# cassowary run -u http://192.168.200.122:8080/ -c 1 -n 1000000 --json-metrics --json-metrics-file=$OUTPUT_FILE

# Zig version. It can take a much larger load than any without failure or degradation in performance
# cassowary run -u http://127.0.0.1:8080/ -c 100 -n 1000000 --json-metrics --json-metrics-file=$OUTPUT_FILE

cassowary run -u http://127.0.0.1:8080/ -c 30 -n 1000000 --json-metrics --json-metrics-file=$OUTPUT_FILE


