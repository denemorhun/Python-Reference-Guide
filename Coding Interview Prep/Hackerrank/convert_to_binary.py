# Convert decimal to binary

def convert_to_binary(n) -> int:

    stack = []

    while n > 0:
        remainder = n % 2
        stack.append(remainder)
        n = n // 2

    stack.reverse()

    return convert_list_to_string(stack)

def convert_list_to_string(arr):
    return "".join(map(str, arr))

if __name__ == '__main__':
        input = 300

        result = convert_to_binary(input)

        print(result)