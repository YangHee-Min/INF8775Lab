import matplotlib.pyplot as plt
import numpy as np

from execute import execute


methods = {
    0: "Conventionnelle",
    1: "Strassen",
    2: "Strassen avec Seuil"
}


def test_puissance(x, y, method: str):
    log_x = np.log2(x)
    log_y = np.log2(y)

    plt.plot(log_x, log_y, linewidth=2.0)
    plt.title(f"Test Puissance algo {methods[method]}")
    plt.xlabel('taille (log)')
    plt.ylabel('temps (log)')
    plt.show()


if __name__ == "__main__":
    list_exemplaire = {
        ("ex2_0", "ex2_1"),
        ("ex3_0", "ex3_1"),
        ("ex4_0", "ex4_1"),
        ("ex5_0", "ex5_1"),
        ("ex6_1", "ex6_2"),
    }
    for method in range(3):
        list_times = []
        list_size = []
        i = 2
        for (ex1, ex2) in list_exemplaire:
            print(ex1, ex2)
            time_execute = execute(ex1, ex2, method)
            list_times.append(time_execute)
            list_size.append(2**i)
            i += 1
        test_puissance(list_size, list_times, method)
        print("x:  ", list_size)
        print("y:  ", list_times)
