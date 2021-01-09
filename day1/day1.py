def get_product_of_two_num_sum_2020(input_list : list):
    for i in input_list:
        if 2020 - i in input_list:
            return (2020 - i) * i

def get_product_of_three_num_sum_2020(input_list : list):
    for i in range(len(input_list) - 2):
        for j in range(1, len(input_list) - 1):
            for k in range(2, len(input_list)):
                # print(i, " , ", j, " , ", k)
                if input_list[i] + input_list[j] + input_list[k] == 2020:
                    return i * j * k

def main():
    # read input as an int list
    input_list = [int(i) for i in open('input.txt').read().splitlines()]
    
    # part 1
    print("(part 1) Answer is: ", get_product_of_two_num_sum_2020(input_list))
    
    # part 2
    print("(part 2) Answer is: ", get_product_of_three_num_sum_2020(input_list))


if __name__ == "__main__":
    main()