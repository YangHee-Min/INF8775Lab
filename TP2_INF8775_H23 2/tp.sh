#!/bin/bash

# Définition des options
while getopts ":a:e:pt" opt; do
  case $opt in
    a) algo="$OPTARG";;
    e) path="$OPTARG";;
    p) is_print=false;;
    t) is_time=false;;
    \?) echo "Option invalide: -$OPTARG" >&2;;
  esac
done

# Vérification des options obligatoires
if [ -z "$algo" ] || [ -z "$path" ]; then
  echo "Usage: ./tp.sh -a ALGORITHME -e CHEMIN_EXEMPLAIRE [-p] [-t]"
  exit 1
fi

python argparser.py -a "$algo" -e1 "$path" $is_print $is_time