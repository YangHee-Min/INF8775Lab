import numpy as np
import math
import matplotlib.pyplot as plt

m_values = []
b_values = []
c_values = []

colors = ["r", "y", "g"]
limit_colors = ["navy", "darkblue", "mediumblue"]

methods = {
    0: "Conventionnelle",
    1: "Strassen",
    2: "Strassen avec Seuil"
}

def test_puissance(x_values, y_values, i):
    x = np.log2(x_values)
    y = np.log2(y_values)
    
    m = (np.mean(x) * np.mean(y) - np.mean(x * y)) / \
            (np.mean(x) ** 2 - np.mean(x ** 2)) 
    b = np.mean(y) - m * np.mean(x)
    
    # m = float(math.floor(m))
    
    m_values.append(m)
    b_values.append(b)
    c_values.append(2**b)
    
    def predict(x, m, b):
        return m*x + b
    
    plt.scatter(x, y, color=limit_colors[i], label=f"Valeurs de la Methode {methods[i]}")
    plt.plot(x, predict(x, m, b), color=colors[i],  linewidth=1.0, label=f"Methode {methods[i]}")
    plt.legend()
    plt.savefig(f"puissance_{methods[i]}.png")
    plt.clf()     

def test_rapport(x_values, y_values, i):
    y = [y/(x**m_values[i]) for x,y in zip(x_values, y_values)]
    # x = x_values
    
    def predict(x, y, m):
        return y/(x**m)
    
    limite_a = [c_values[i] for j in range(len(x_values))]
    
    plt.plot(x_values[1:], limite_a[1:], color=limit_colors[i], label=f"Valeurs Limite de la Methode {methods[i]}")
    plt.plot(x_values[1:], y[1:], color=colors[i],  linewidth=1.0, label=f"Methode {methods[i]}")
    plt.legend()
    plt.savefig(f"rapport_{methods[i]}.png")
    plt.clf()
    
def test_constante(x_values, y_values, i):
    def predict(x, m):
        return (x**m)
    
    x =np.power(x_values, m_values[i])
    
    # Trouver B
    b = 0 
    
    def function(x, c):
        return c*x + b
    
    plt.scatter(x, y_values, color=limit_colors[i], label=f"Valeurs des pairs de la Methode {methods[i]}")
    plt.plot(x, function(x, c_values[i]), color=colors[i],  linewidth=1.0, label=f"Methode {methods[i]}")
    plt.legend()
    plt.savefig(f"constante_{methods[i]}.png")
    plt.clf()

if __name__ == "__main__":
    data_set = {
        0: (
            [8, 16, 32, 64, 128, 256, 512], 
            [456000, 3340000, 26148000, 211442000, 1673018000, 13281119000, 106125677000]
            ), 
        1: (
            [8, 16, 32, 64, 128, 256, 512], 
            [436000, 3285000, 26395000, 209706000, 1666750000, 13260289000, 107042382000]
            ), 
        2: (
            [8, 16, 32, 64, 128, 256, 512], 
            [437000, 3276000, 26017000, 211016000, 1658345000, 13325773000, 106231073000]
            )
        }

    for i in range(3):
        x, y = data_set[i]
        test_puissance(x, y, i)
        test_rapport(x, y, i)
        test_constante(x, y, i)

"""
 {
        0: (
            [8, 16, 32, 64, 128, 256, 512], 
            [456000, 3340000, 26148000, 211442000, 1673018000, 13281119000, 106125677000]
            ), 
        1: (
            [8, 16, 32, 64, 128, 256, 512], 
            [436000, 3285000, 26395000, 209706000, 1666750000, 13260289000, 107042382000]
            ), 
        2: (
            [8, 16, 32, 64, 128, 256, 512], 
            [437000, 3276000, 26017000, 211016000, 1658345000, 13325773000, 106231073000]
            )
        }
"""
