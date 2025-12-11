#!/bin/bash

if [ $# -eq 0 ]; then
    python3 -m src.main puzzles/example.json
else
    python3 -m src.main $1
fi
