import matplotlib.pyplot as plt
import numpy as np
import csv

from execute import execute


methods = {
    0: "Conventionnelle",
    1: "Strassen",
    2: "Strassen avec Seuil"
}


def test_puissance(dataset):
    fig, axs = plt.subplots(3)
    fig.suptitle("Test de puissance")

    # slopes = []
    exponentials = []
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
        exponentials.append(m)
    plt.savefig('puissance.png')
    plt.show()
    return (exponentials)


def test_rapport(dataset, exponents):
    fig, axs = plt.subplots(3)
    fig.suptitle("Test de rapports")

    for i in range(3):
        data = dataset[i]
        x, y = data[0], data[1]
        f_x = [polynomial(x_ele, exponents[i]) for x_ele in x]

        y_over_f_x = [y[j]/f_x[j] for j in range(len(y))]

        axs[i].plot(x, y_over_f_x, color='red',  linewidth=2.0)
        axs[i].set_title(f"Methode {methods[i]}")

    plt.savefig('rapport.png')
    plt.show()
    return


def test_constantes(dataset):
    fig, axs = plt.subplots(3)
    fig.suptitle("Test des constantes")

    for i in range(3):
        data = dataset[i]
        x, y = data[0], data[1]
        f_x = [polynomial(x_ele, exponents[i]) for x_ele in x]

        axs[i].plot(f_x, y, color='red',  linewidth=2.0)
        axs[i].set_title(f"Methode {methods[i]}")

    plt.savefig('constantes.png')
    plt.show()
    return


def polynomial(x, exponent, slope=1):
    return slope * x ** exponent


def write_csv(data_set):
    for i in range(3):
        # name of the csv file
        name = methods[i].replace(" ", "")
        filename = f"{name}-results.csv"

        x = np.array(data_set[i][0])
        y = np.array(data_set[i][1])

        new_array = np.column_stack((x, y))

        # writing to the csv file
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(new_array)


if __name__ == "__main__":
    data_set = {}
    list_exemplaire = []

    MIN_MATRIX_SIZE = 3
    NUM_SIZE = 6
    MAX_MATRIX_SIZE = MIN_MATRIX_SIZE + NUM_SIZE - 1
    EXAMPLE_COUNT = 5

    for method in range(3):
        print(methods[method])
        data_set[method] = []
        list_size = []
        list_times = []
        for size in range(MIN_MATRIX_SIZE, MAX_MATRIX_SIZE + 1):
            print(f"\t{methods[method]}Size: {size}")
            sub_array = []
            for i in range(EXAMPLE_COUNT):
                for j in range(EXAMPLE_COUNT):
                    ex1, ex2 = (f"ex{size}_{i}", f"ex{size}_{j}")
                    time_execute = execute(ex1, ex2, method)
                    sub_array.append(time_execute)
                    print(f"\t\tex{size}_{i}, ex{size}_{j}: {time_execute}ms")
            list_size.append(2**size)
            list_times.append((sum(sub_array)/len(sub_array)))
        data_set[method] = (list_size, list_times)

    exponents = []
    (exponents) = test_puissance(data_set)
    test_rapport(data_set, exponents)
    test_constantes(data_set)

    write_csv(data_set)
