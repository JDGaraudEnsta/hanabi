#!/bin/bash

for i in $(seq 1 $*); do
    hanabi --ai=Cheater |grep score |sed -e 's/.*is //'
done

