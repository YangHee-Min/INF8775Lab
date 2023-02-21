import argparse
import os.path
import sys
from execute import execute

parser = argparse.ArgumentParser(
    description='Faire une opération sur deux fichiers de matrices.')
parser.add_argument('-a', dest='algo', required=True,
                    choices=['conv', 'strassen', 'strassenSeuil'], help='l\'algorithme à utiliser')
parser.add_argument('-e1', dest='path1', required=True, type=str,
                    help='chemin absolu du premier fichier de matrice')
parser.add_argument('-e2', dest='path2', required=True, type=str,
                    help='chemin absolu du deuxième fichier de matrice')
parser.add_argument('-p', dest='print', action='store_true',
                    help='true affiche la matrice résultat sans texte superflu. False par défaut')
parser.add_argument('-t', dest='time', action='store_true',
                    help='true affiche le temps d\'exécution en millisecondes. False par défaut')

# Verify that the files exist


def check_file_exists(path):
    if not os.path.isfile(path):
        print(f'Erreur : Le fichier {path} n\'existe pas.')
        sys.exit(1)


# Parse arguments
args = parser.parse_args()
check_file_exists(args.path1)
check_file_exists(args.path2)

# Execute wanted algorithm
execute(args.path1, args.path2, method=args.algo,
        is_time=args.print, is_print=args.time)