import argparse
import os.path
import sys
from main import execute

parser = argparse.ArgumentParser(
    description='Trouver le plus petit chemin .')
parser.add_argument('-a', metavar='a', required=True, action='store',
                    choices=['glouton', 'progdyn', 'approx'], help='l\'algorithme à utiliser')
parser.add_argument('-e', metavar='e', required=True, action='store', type=str,
                    help='chemin absolu des villes a visiter')
parser.add_argument('-p', dest='print', action='store_true',
                    help='true affiche le chemin résultat sans texte superflu. False par défaut')
parser.add_argument('-t', dest='time', action='store_true',
                    help='true affiche le temps d\'exécution en millisecondes. False par défaut')

# Verify that the files exist
def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        print(f'Erreur : Le fichier {file_path} n\'existe pas.')
        sys.exit(1)

# Parse arguments
args = parser.parse_args()
check_file_exists(args.e)

# Execute wanted algorithm
execute(args.e, method=args.a,
        is_time=args.time, is_print=args.print)