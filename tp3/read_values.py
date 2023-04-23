import os.path

def verify_path(filename: str):
    if not os.path.exists(filename):
        raise Exception("Le fichier n'existe pas");

def read_values(filename: str):
    verify_path(filename)
    
    f = open("demofile.txt", "r")
    N, M, K = f.readline().split(' ')
    m_set = f.readline().split(' ')
    size_enclos = []
    
    
    