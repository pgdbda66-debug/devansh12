print("Hello from Code file")


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


dbda@dbda-virtualbox:~$ cat case.sh

#!/bin/bash

while (True); do

echo "1. date"

echo "2. calendar"

echo "3. list files"

echo "4. Exit"

read -p choose an option:" num

case Snum in

1)

echo date is $(date)"

echo $(cal)"

echo files in current directory $(Ls)"

echo "exit program..." break

echo "enter a valid command"

esac done

dbda@dbda-virtualbox:-5./case.sh
