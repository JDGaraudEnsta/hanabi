#!/bin/bash

python3 hanabi_unittest.py || { echo "hanabi_unittest.py failed. Exiting now." ; exit 1 ; }

for f in game*.py; do
    hanabi <<< ">self.load('$f')" |tee $f.log
done

declare -A scores

scores=(
    ["game1.py"]=4
    ["game2.py"]=20
    ["game3.py"]=24
    ["game4.py"]=25
    ["game5.py"]=21
    ["game6.py"]=21
    )

failed=0

echo
echo "========= Summary ==========="
printf "%-10s %s %s  %s\n" test score ref status
for f in game*.py; do
    score=$(grep 'Your score is' $f.log | sed -e 's/.*is //')
    ref=${scores[$f]}
    if [ -z "$ref" ]; then
        stat="\033[43m No ref \033[0m"
    elif [ $score -eq $ref ]; then
        stat="  Ok  "
        stat="\033[42m   Ok   \033[0m"
    else
        stat="Failed"
        stat="\033[41m Failed \033[0m"
        let failed+=1
    fi
    printf "%-10s %5i %3i %b \n" $f "$score" "$ref" "$stat"
done

exit $failed
