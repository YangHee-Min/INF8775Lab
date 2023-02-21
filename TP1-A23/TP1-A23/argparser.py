import argparse
import os.path
import sys
import time

# Créer un parseur avec les options requises
parser = argparse.ArgumentParser(description='Faire une opération sur deux fichiers de matrices.')
parser.add_argument('-a', dest='algo', required=True, choices=['conv', 'strassen', 'strassenSeuil'], help='l\'algorithme à utiliser')
parser.add_argument('-e1', dest='path1', required=True, type=str, help='chemin absolu du premier fichier de matrice')
parser.add_argument('-e2', dest='path2', required=True, type=str, help='chemin absolu du deuxième fichier de matrice')
parser.add_argument('-p', dest='print', action='store_true', help='affiche la matrice résultat sans texte superflu')
parser.add_argument('-t', dest='time', action='store_true', help='affiche le temps d\'exécution en millisecondes')

# Vérifier que les fichiers existent
def check_file_exists(path):
    if not os.path.isfile(path):
        print(f'Erreur : Le fichier {path} n\'existe pas.')
        sys.exit(1)

# Parser les arguments
args = parser.parse_args()
check_file_exists(args.path1)
check_file_exists(args.path2)

# Lire les matrices depuis les fichiers
with open(args.path1, 'r') as f:
    mat1 = [[float(num) for num in line.split()] for line in f.readlines()]
with open(args.path2, 'r') as f:
    mat2 = [[float(num) for num in line.split()] for line in f.readlines()]

# Vérifier que les matrices ont les mêmes dimensions
if len(mat1) != len(mat2) or any(len(mat1[i]) != len(mat2[i]) for i in range(len(mat1))):
    print('Erreur : Les matrices n\'ont pas les mêmes dimensions.')
    sys.exit(1)

# Exécuter l'algorithme demandé
start_time = time.time()
if args.algo == 'conv':
    result = [[sum([mat1[i][k] * mat2[k][j] for k in range(len(mat1))]) for j in range(len(mat2[0]))] for i in range(len(mat1))]
elif args.algo == 'strassen':
    # TODO: Exécuter l'algorithme de Strassen
    result = mat1
elif args.algo == 'strassenSeuil':
    # TODO: Exécuter l'algorithme de Strassen avec seuil
    result = mat1
end_time = time.time()

# Afficher la matrice résultat, avec ou sans texte superflu
if args.print:
    for line in result:
        print(' '.join(str(num) for num in line))
else:
    print('Résultat :')
    for line in result:
        print(' | '.join(str(num) for num in line))

# Afficher le temps d'exécution, avec ou sans texte superflu
if args.time:
    print(f'Temps d\'exécution : {(end_time - start_time) * 1000:.2f} ms')
else:
    print(f'Temps d\'exécution : {(end_time - start_time):.2f} secondes')