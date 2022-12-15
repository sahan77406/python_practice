# An implementation of MergeSort
def merge_sorting(array1):

    # Checking if the length of array greater than 1

    if len(array1) > 1:

        # Finding the mid of the array

        mid_array = len(array1)//2

    # Dividing the array elements

        left_array = array1[:mid_array]

        right_array = array1[mid_array:]

    # Sorting the both halves

        merge_sorting(left_array)

        merge_sorting(right_array)

        a = b = c = 0

    # Copy data to temp arrays left_array[] and right_array[]

        while a < len(left_array) and b < len(right_array):
            if left_array[a] <= right_array[b]:
                array1[c] = left_array[a]
                a += 1
            else:
                array1[c] = right_array[b]
                b += 1
            c += 1

    # Checking if any element was left

        while a < len(left_array):

            array1[c] = left_array[a]
            a += 1
            c += 1

        while b < len(right_array):

            array1[c] = right_array[b]
            b += 1
            c += 1

    # print the array


def print_array(array):

    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':

    array = [90, -1, 17, 4, 6, 101, -2]

    print_array(array)
    merge_sorting(array)
    print_array(array)
