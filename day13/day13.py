def day13_part1(input_txt):
    arrive_time = int(input_txt[0])
    bus_nums = []
    for i in input_txt[1].split(','):
        if i.isdigit():
            bus_nums.append(int(i))
    bus_depart_time_dict = {}
    for num in bus_nums:
        n = 1
        departure_time = num
        while departure_time < arrive_time:
            n += 1
            departure_time = n * num

        bus_depart_time_dict[num] = departure_time
    earliest_bus_num = min(bus_depart_time_dict, key=bus_depart_time_dict.get)
    wait_time = bus_depart_time_dict[earliest_bus_num] - arrive_time
    return (wait_time * earliest_bus_num)

def find_ans(bus_dict, start_val, max_key):
    for dict_idx, (dict_val_idx, dict_val) in enumerate(bus_dict.items()):
        if (start_val - dict_val_idx) % dict_val == 0:
            if dict_idx == max_key-1:
                return start_val
        else:
            return False

def day13_part2(input_txt):
    bus_schedule = input_txt[1].split(',')
    bus_dict = {}
    for idx, bus_num in enumerate(bus_schedule):
        if bus_num.isdigit():
            bus_dict[idx] = int(bus_num)
    offset = 0
    max_key = max(bus_dict)
    max_val_idx = max(bus_dict, key=bus_dict.get)
    max_val = bus_dict[max(bus_dict, key=bus_dict.get)]
    del bus_dict[max_val_idx]

    offset_multiple = int(offset / max_val)
    start_val = offset_multiple * max_val + max_val_idx

    while True:
        ans = find_ans(bus_dict, start_val, max_key)
        print(ans)
        if not ans:
            offset_multiple += 1
            start_val = offset_multiple * max_val + max_val_idx
            print('start_val: ', start_val)
        else:
            return ans

def main():
    input_txt = open('input.txt').read().splitlines()
    # print('day 13 part 1: ', day13_part1(input_txt))
    day13_part2(input_txt)
            
if __name__ == "__main__":
    main()