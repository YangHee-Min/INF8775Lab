#!/bin/bash

is_print=false

# Définition des options
while getopts ":e:p" opt; do
  case $opt in
    e) path="$OPTARG";;
    p) is_print=true;;
    \?) echo "Option invalide: -$OPTARG" >&2;;
  esac
done

# Vérification des options obligatoires
if [ -z "$path" ]; then
  echo "Usage: ./tp.sh -e CHEMIN_EXEMPLAIRE [-p]"
  exit 1
fi

python argparser.py -e "$path" ${is_print:+-p}