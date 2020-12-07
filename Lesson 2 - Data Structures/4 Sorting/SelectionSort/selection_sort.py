# Bubble sort algorithm
'''
Selection Sort [Best/Worst: O(N^2)]
Scan all items and find the smallest. Swap it into position as the first item. Repeat the selection sort on the remaining N-1 items.

I found this the most intuitive and easiest to implement — you always iterate forward (i from 0 to N-1), and swap with the smallest element (always i).
'''

def selectsort(dataset):
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
