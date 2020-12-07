# Bubble sort algorithm


def bubbleSort(dataset):
    # TODO: start with the array length till 0th element and decrement by 1

    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            # if value j > j+1, swap adjacent
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp


    print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
