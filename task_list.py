def validation():
    while True:
        try:
            input_list = sorted(set([int(i) for i in input('Enter comma-separated integers:\n').split(',')]))
            return input_list
        except (TypeError, ValueError):
            print("Incorrect input, try again")
            continue

def get_ranges(input_list):
    min_index = 0
    string_1 = ''

    def string_2(max_index):
        if min_index == max_index:
            return str(input_list[min_index])
        else:
            return str(input_list[min_index]) + '-' + str(input_list[max_index]) 

    for i in range(1, len(input_list)):
        if input_list[i] - input_list[i - 1] != 1:
            string_1 += string_2(i-1) + ', '
            min_index = i
    string_1 += string_2(i)
    return string_1

print(get_ranges(validation()))