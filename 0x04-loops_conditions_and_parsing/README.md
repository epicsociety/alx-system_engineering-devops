Loops on shell.
Shell scripting 
shell permissions
for, while, until loops
if statement on shell

----------------------------------
for loops
-----------------------------------
for i in 1 2 3 4 5; do COMMANDS; done

for i in {startingpoint..endingpoint..increment}; do COMMANDS; done

for NAME [ in LIST ]; do COMMANDS; done
-------------------------------
while loops
-------------------------------
while [condition is true]; do COMMANDS; increment; done

example 1: =======

num=0

while [ $num -lt 10 ]
do
        echo "Niice"
	num=$(( num + 1))
done

example 2: ===========
number=1; while [ $number -lt 10 ]; do echo "School is good"; number=$(( number + 1 )); done



