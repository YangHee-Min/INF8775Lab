import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

from execute import execute
from method import Method

def taux_moyen(x, y):
    somme = 0
    j = 0.
    for i in range(0, len(x) - 16, 16):
        print("hello")
        somme += (y[i+16] - y[i])/(x[i+16] - x[i])
        j += 1
    print(j)
    return somme/j

def test_puissance(points, i):
    x_values = []
    y_values = []
    for (x, y) in points:
        x_values.append(math.log(x,2))
        y_values.append(math.log(y, 2))
    
    m = taux_moyen(x_values, y_values)
    
    modele = []
    
    for x_value in x_values:
        modele.append(m * x_value)
    
    print(x_value)
    print(y_values)
    print(modele)
    
    axs[i].plot(x_values, y_values, 'r+')
    axs[i].plot(x_values, modele,'b-',label='modèle linéaire')
    axs[i].grid()
    return m
    

def test_rapport(points, m, i):
    x_values = []
    y_values = []
    
    for (x, y) in points:
        x_values.append(x)
        y_theorical = x**m
        y_values.append(y/y_theorical)
    
    def objective(x, a):
        return a*(x**m)

    popt, _ = curve_fit(objective, x_values, y_values)
    a = popt
    
    modele = objective(x_values, a)
    
    axs[i].plot(x_values, y_values, 'r+')
    axs[i].plot(x_values, modele,'b-',label='modèle linéaire')
    axs[i].grid()
    
    return a
    

if __name__ == '__main__':
    data_set = {}
    m_values = {}
    a_values = {}
    
    fig, axs = plt.subplots(3)
    fig.suptitle("Test de puissance")
    
    for method in range(3):
        data_set[method]= []
        list_size= []
        list_times = []
        for size in range(2,8):
            sub_array = []
            for i in range(4):
                for j in range(4):
                    ex1, ex2 = (f"ex{size}_{i}", f"ex{size}_{j}")
                    time_execute = sub_array.append(execute(ex1, ex2, method))
            list_size.append(2**size)
            list_times.append((sum(sub_array)/len(sub_array)))
        data_set[method] = (list_size, list_times)
        print(f"Data array for method {method} : ", data_set[method])
        m = test_puissance(data_set[method], method)
        print("m = ", m)
        m_values[method] = m
    plt.show()
    
    fig, axs = plt.subplots(3)
    fig.suptitle("Test de Rapport")
    
    for method in range(3):
        a = test_rapport(data_set[method], m_values[method], method)
        print("a = ", a)
        a_values[method] = a
    plt.show()
    
    
    
        
    