#!/bin/bash

nb=$1
nb_players=$2

if [ -z "$nb" ]; then
    nb=10
fi

if [ -z "$nb_players" ]; then
    nb_players=2
fi

for i in $(seq 1 $nb); do
    score=$(hanabi -n $nb_players --ai=Cheater |grep score |sed -e 's/.*is //')
    echo $score
    if [ $score -lt 25 ]; then
        cp autosave.py gamelost$i.py
    fi
done

