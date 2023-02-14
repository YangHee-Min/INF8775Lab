import matplotlib.pyplot as plt
import numpy as np

from execute import execute


methods = {
    0: "Conventionnelle",
    1: "Strassen",
    2: "Strassen avec Seuil"
}


def test_puissance(dataset):
    fig, axs = plt.subplots(3)
    fig.suptitle("Test de puissance")
    
    for i in range(3):
        data = dataset[i]
        axs[i].plot(np.log2(data[0]), np.log2(data[1]), linewidth=2.0)
        axs[i].set_title(f"Methode {methods[i]}")
        #axs[i].xlabel('taille (log2)')
        #axs[i].ylabel('temps (log10)')

    plt.show()
    return 


if __name__ == "__main__":
    data_set = {}
    list_exemplaire = []
    for i in range(2, 9):
        list_exemplaire.append((f"ex{i}_0", f"ex{i}_1"))
    for method in range(3):
        list_times = []
        list_size = []
        i = 2
        for j in range(len(list_exemplaire)):
            ex1, ex2 = list_exemplaire[j]
            print(ex1, ex2)
            time_execute = execute(ex1, ex2, method)
            list_times.append(time_execute)
            list_size.append(2**i)
            i += 1
        data_set[method] = (list_size, list_times)
    test_puissance(data_set)
