#!/bin/bash

nb=$*

if [ -z "$nb" ]; then
    nb=10
fi

for i in $(seq 1 $nb); do
    score=$(hanabi --ai=Cheater |grep score |sed -e 's/.*is //')
    echo $score
    if [ $score -lt 25 ]; then
        cp autosave.py gamelost$i.py
    fi
done

