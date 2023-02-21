#!/bin/bash

# Vérifier les arguments
if [[ $# -lt 6 ]]; then
    echo "Usage: $0 -a {conv, strassen, strassenSeuil} -e1 PATH_VERS_EX_1 -e2 PATH_VERS_EX_2 [-p] [-t]"
    exit 1
fi

# Analyser les arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -a|--algo)
            algo="$2"
            shift
            shift
            ;;
        -e1)
            path1="$2"
            shift
            shift
            ;;
        -e2)
            path2="$2"
            shift
            shift
            ;;
        -p|--print)
            print="-p"
            shift
            ;;
        -t|--time)
            time="-t"
            shift
            ;;
        *)
            echo "Option non reconnue : $1"
            exit 1
            ;;
    esac
done

# Vérifier que les fichiers existent
if [[ ! -f "$path1" ]]; then
    echo "Erreur : Le fichier $path1 n'existe pas."
    exit 1
fi
if [[ ! -f "$path2" ]]; then
    echo "Erreur : Le fichier $path2 n'existe pas."
    exit 1
fi

# Appeler le script Python avec les arguments
python execute.py -a "$algo" -e1 "$path1" -e2 "$path2" "$print" "$time"