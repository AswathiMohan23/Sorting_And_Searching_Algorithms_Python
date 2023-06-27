def ascending(input_list, length_of_list):
    for i in range(length_of_list):
        for j in range(0, length_of_list - i - 1):
            if input_list[j] > input_list[j + 1]:
                (input_list[j+1], input_list[j]) = (input_list[j], input_list[j+1])


if __name__ == "__main__":
    input_list = [4, 3, 2, 1]
    length=len(input_list)
    ascending(input_list, length)
    print(input_list)
