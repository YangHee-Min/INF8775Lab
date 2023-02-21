#!/bin/bash

algo=""
path1=""
path2=""
is_print=""
is_time=""

while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -a|--algo)
            algo="$2"
            shift
            shift
            ;;
        -e1|--path1)
            path1="$2"
            shift
            shift
            ;;
        -e2|--path2)
            path2="$2"
            shift
            shift
            ;;
        -p|--is_print)
            is_print="-p"
            shift
            ;;
        -t|--is_time)
            is_time="-t"
            shift
            ;;
        *) 
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

if [[ -z "$algo" || -z "$path1" || -z "$path2" ]]; then
    echo "Missing required arguments. Usage: $0 -a {conv, strassen, strassenSeuil} -e1 PATH_VERS_EX_1 -e2 PATH_VERS_EX_2 [-p] [-t]"
    exit 1
fi

python argparser.py -a "$algo" -e1 "$path1" -e2 "$path2" $is_print $is_time