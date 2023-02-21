import matplotlib.pyplot as plt
import numpy as np
import itertools

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
        (x, y) = (np.log2(data[0]), np.log2(data[1]))

        # Calculate the slope and y-intercept of the regression line
        m = (np.mean(x) * np.mean(y) - np.mean(x * y)) / \
            (np.mean(x) ** 2 - np.mean(x ** 2))
        b = np.mean(y) - m * np.mean(x)

        def predict(x, m, b):
            return m * x + b
        axs[i].scatter(x, y, color='blue')
        axs[i].plot(x, predict(x, m, b), color='red',  linewidth=2.0)
        axs[i].set_title(f"Methode {methods[i]}")

    plt.show()
    return


if __name__ == "__main__":
    data_set = {}
    list_exemplaire = []

    MIN_MATRIX_SIZE = 3
    NUM_SIZE = 7
    MAX_MATRIX_SIZE = MIN_MATRIX_SIZE + NUM_SIZE - 1
    EXAMPLE_COUNT = 5

    for method in range(3):
        print(methods[method])
        data_set[method] = []
        list_size = []
        list_times = []
        for size in range(MIN_MATRIX_SIZE, MAX_MATRIX_SIZE):
            print(f"\tSize: {size}")
            sub_array = []
            for i in range(EXAMPLE_COUNT):
                for j in range(EXAMPLE_COUNT):
                    print(f"\t\tex{size}_{i}, ex{size}_{j}")
                    ex1, ex2 = (f"ex{size}_{i}", f"ex{size}_{j}")
                    time_execute = sub_array.append(execute(ex1, ex2, method))
            list_size.append(2**size)
            list_times.append((sum(sub_array)/len(sub_array)))
        data_set[method] = (list_size, list_times)

    test_puissance(data_set)
