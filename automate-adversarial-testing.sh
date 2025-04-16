#!/usr/bin/env bash

models="smollm2:1.7b granite3.1-moe:1b granite3.1-moe:latest granite3.1-dense:2b llama3.1:70b llama3.1:latest llama3.2:1b mistral-nemo:12b qwen2.5:1.5b qwen2.5:7b qwen2.5:72b"

read -p "Hello! How can I help you today? " user_input

for model in $models
do
    for item in {1..100} # Note: lama3.1:70b and qwen2.5:72b was only executed 10 times due to hardware restrictions.
    do
        echo "$model run $item"
        echo "$user_input" | /home/smannan/Documents/thesis-llm-attacks-12-influence-llm-context-using-tool-calls/ollama/bin/python tooling.py $model
    done
done