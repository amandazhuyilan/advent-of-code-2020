
import numpy as np
# import pdb; pdb.set_trace()

def update_seat_chart_part1(A: np.ndarray):
    is_updated = False
    new_occupied_index = []
    new_vaccant_index = []
    # check the two given rules and update the indicies that need to be changed to and from occupied/vaccant into lists 
    for row in range(1, A.shape[0] - 1):
        for col in range(1, A.shape[1] - 1):
            if A[row][col] == 'L' or '#':
                count_occupied_arr = np.array([A[row-1][col-1], A[row-1][col], A[row][col-1], A[row+1][col+1], A[row][col+1], A[row+1][col], A[row-1][col+1], A[row+1][col-1]])
                if A[row][col] == 'L' and np.count_nonzero(count_occupied_arr == '#') == 0:
                    new_occupied_index.append((row, col))
                    is_updated = True

                if A[row][col] == '#' and np.count_nonzero(count_occupied_arr == '#') >= 4:
                    new_vaccant_index.append((row, col))
                    is_updated = True

    # update, in-place, vaccant and occupied for elements in A
    for indicies in new_occupied_index:
        A[indicies[0]][indicies[1]] = '#'
    for indicies in new_vaccant_index:
        A[indicies[0]][indicies[1]] = 'L'

    if is_updated == True:
        return True
    else:
        return False

def update_seat_chart_part2(A: np.ndarray):
    is_updated = False
    new_occupied_index = []
    new_vaccant_index = []
    # check the two given rules and update the indicies that need to be changed to and from occupied/vaccant into lists 
    for row in range(1, A.shape[0] - 1):
        for col in range(1, A.shape[1] - 1):
            if A[row][col] == 'L' or '#':
                for n in range(1, lambda x ,y: min(A.shape[0] - 1, A.shape[1] - 1))
                # get the 8 direction symbols as individual lists
                    down_left_list.append(A[row-n][col-n])
                    down_list.append(A[row-n][col])
                    down_right_list.append(A[row-n][col+n])
                    left_list.append(A[row][col-n])
                    right_list.append(A[row][col+n])
                    up_list.append(A[row+n][col])
                    up_left_list.append(A[row+n][col-n])
                    up_right_list.append(A[row+n][col+n])
                
                # [TODO] in each list, push the first occuring "L" or "#" of the above lists into a new array
                # [TODO] according to the number of "#" and 'L' in the array, use count_nonzero to count the 'L' and '#', do the rest same as part1
            
                # count_occupied_arr = np.array([A[row-1][col-1], A[row-1][col], A[row][col-1], A[row+1][col+1], A[row][col+1], A[row+1][col], A[row-1][col+1], A[row+1][col-1]])

                if A[row][col] == 'L' and np.count_nonzero(count_occupied_arr == '#') == 0:
                    new_occupied_index.append((row, col))
                    is_updated = True

                if A[row][col] == '#' and np.count_nonzero(count_occupied_arr == '#') >= 5:
                    new_vaccant_index.append((row, col))
                    is_updated = True

    # update, in-place, vaccant and occupied for elements in A
    for indicies in new_occupied_index:
        A[indicies[0]][indicies[1]] = '#'
    for indicies in new_vaccant_index:
        A[indicies[0]][indicies[1]] = 'L'

    if is_updated == True:
        return True
    else:
        return False

def main():
    # read input as array of arrays
    A = np.loadtxt('input.txt', dtype='str')
    B = np.full((A.size + 2, len(A[0]) + 2), '.')

    for row in range(A.size):
        for col in range(len(A[0])):
            B[row + 1][col + 1] = A[row][col]

    print("FIRST B:")
    print(B)
    condition = True
    times = 0
    while condition:
        condition = update_seat_chart(B)
        times = times + 1
    # end of loop

    occupied_seat = 0
    for row in range(1, B.shape[0]-1):
        for col in range(1, len(B[0])-1):
            if B[row][col] == '#':
                occupied_seat += 1
    
    print("occupied seat: ", occupied_seat)


if __name__ == "__main__":
    main()