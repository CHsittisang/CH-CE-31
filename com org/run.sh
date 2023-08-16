#!/bin/bash

# Read input from user for folder name
read -p "Enter folder name: " folder_name

if [ ! -d "$folder_name" ]; then
    echo "No such file or directory."
    exit 0
fi

cd "$folder_name"

cr=echo $'\n.'
cr=${cr%.}

# while true; do
#     read -p " 1: asm $cr 2: gcc $cr 3: exit $cr>> " choice

#     case $choice in
#     1)
        as -o program.o program.s
        ld -o program program.o
#         break
#         ;;
#     2)
        # as -g -o program.o program.s
        # gcc -o program program.o
#         break
#         ;;
#     3)
#         # echo "kuy!"
#         exit 0
#         ;;
#     *)
#         echo "Invalid choice"
#         ;;
#     esac
# done

# Run the resulting executable
# ./program ; echo $?
./program

# Change back to the original directory
cd ..