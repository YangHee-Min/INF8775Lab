import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

m_values = []
b_values = []
c_values = []

colors = ["r", "y", "g"]
limit_colors = ["navy", "darkblue", "mediumblue"]

methods = {
    0: "Glouton",
    1: "MST",
    2: "dynamique"
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

    fig, ax = plt.subplots()
    fig.suptitle(f"Test de puissance de la methode {methods[i]}")
    ax.set_ylabel('Temps (ns) - Log')
    ax.set_xlabel('Taille - Log')

    ax.scatter(x, y, color=limit_colors[i], label=f"Valeurs obtenues")
    ax.plot(x, predict(x, m, b),
            color=colors[i],  linewidth=1.0, label=f"Modèle estimé")
    ax.legend()

    # Add equation of the predict function to the figure
    eqn = rf"$y = {m:.2f}x + {b:.2f}$"
    ax.text(0.70, 0.05, eqn, transform=ax.transAxes, fontsize=12,
            verticalalignment='bottom')

    fig.savefig(f"puissance_{methods[i]}.png")
    plt.clf()


def test_rapport(x_values, y_values, i):
    y = [y/(x**m_values[i]) for x, y in zip(x_values, y_values)]

    fig, ax = plt.subplots()
    fig.suptitle(f"Test de rapport de la methode {methods[i]}")
    ax.set_ylabel('Temps (ns)')
    ax.set_xlabel('Taille')
    ax.scatter(x_values[1:], y[1:], color=limit_colors[i],
               linewidth=1.0, label=f"Modèle estimé")

    # fit a polynomial curve to the data
    coeffs = np.polyfit(x_values[1:], y[1:], deg=2)
    curve_func = np.poly1d(coeffs)

    # plot the polynomial curve with the specified color
    x_range = np.linspace(min(x_values[1:]), max(x_values[1:]), 100)
    ax.plot(x_range, curve_func(x_range), color=colors[i],
            label=f"Modèle estimé degré 2")

    # Adjust the position of the legend
    ax.legend()

    # Add equation of the predict function to the figure
    eqn = rf"$y = {coeffs[0]:.3f}x^2 + {coeffs[1]:.3f}x + {coeffs[2]:.3f}$"
    ax.text(0.7, 0.05, eqn, transform=ax.transAxes, fontsize=12,
            verticalalignment='bottom', horizontalalignment='right')

    fig.savefig(f"rapport_{methods[i]}.png")
    plt.clf()


def test_constante(x_values, y_values, i):
    x = np.power(x_values, m_values[i])

    def function(x, c):
        return c*x

    fig, ax = plt.subplots()
    fig.suptitle(f"Test de constante de la methode {methods[i]}")
    ax.set_ylabel('Temps (ns)')
    ax.set_xlabel('Taille')
    ax.scatter(x, y, color=limit_colors[i], label=f"Valeurs obtenues")

    ax.plot(x, function(x, c_values[i]), color=colors[i],
            linewidth=1.0, label=f"Modèle estimé")
    ax.legend()

    # Add equation of the predict function to the figure
    eqn = rf"$y = {c_values[i]:.2f}x$"
    ax.text(0.70, 0.05, eqn, transform=ax.transAxes, fontsize=12,
            verticalalignment='bottom')

    fig.savefig(f"constante_{methods[i]}.png")
    plt.clf()


def read_spreadsheet(filename):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(filename)

    # Extract the Size and Execution Time columns as lists
    size_list = df['Size'].tolist()
    execution_time_list = df['Execution Time'].tolist()

    return size_list, execution_time_list


if __name__ == "__main__":
    file_names = ["dyn.xlsx", "dyn.xlsx", "dyn.xlsx"]

    for i, file_name in enumerate(file_names):
        x, y = read_spreadsheet(file_name)
        test_puissance(x, y, i)
        test_rapport(x, y, i)
        test_constante(x, y, i)
