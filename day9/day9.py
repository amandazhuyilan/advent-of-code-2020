def in_preamble(preamble_list : list, num : int) -> bool:
    # returns true if the number is to be found in the preamble_list 
    for idx, preamble_num in enumerate(preamble_list):
        if (num - preamble_num) in preamble_list:
            return True


def main():
    input1 = [int(i) for i in open('input.txt').read().splitlines()]
    
    # part 1 - finding the first invalid num
    for index in range(len(input1) - 25):
        first_25_num_list = input1[index : 25 + index]
        if in_preamble(first_25_num_list, input1[25 + index]):
            continue

        invalid_num = input1[25 + index]
        print('Invalid num is: ', invalid_num)

    # part 2 - sum of min and max of a contiguous set of at least two numbers that adds up to invalid num found in part 1
    for idx_start in range(len(input1) - 2):
        for idx_end in range(idx_start + 1, len(input1) - 1):
            if sum(input1[idx_start : idx_end]) == invalid_num:
                print("min + max = ", max(input1[idx_start : idx_end]) + min(input1[idx_start : idx_end]))

    return

if __name__ == "__main__":
    main()