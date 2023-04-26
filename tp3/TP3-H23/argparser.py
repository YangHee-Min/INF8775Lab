import argparse
import os.path
import sys
from execute import execute

parser = argparse.ArgumentParser(
    description='Trouver le plus petit chemin .')
parser.add_argument('-e', dest='path', required=True, type=str,
                    help='chemin absolu des villes a visiter')
parser.add_argument('-p', dest='print', action='store_true',
                    help='true affiche le chemin résultat sans texte superflu. False par défaut')

# Verify that the files exist


def check_file_exists(path):
    if not os.path.isfile(path):
        print(f'Erreur : Le fichier {path} n\'existe pas.')
        sys.exit(1)


# Parse arguments
args = parser.parse_args()
# check_file_exists(args.path)

# Execute wanted algorithm
execute(args.path,
        is_print=args.print)
