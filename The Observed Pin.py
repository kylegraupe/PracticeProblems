import itertools
def get_pins(observed):
    key_pad2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]] # List of Lists containing Keypad
    obs_list = [int(x) for x in observed]  # List Containing Ints from observed string input
    variations = [[] for p in range(len(obs_list))]  # Creates List of Lists with the same length as obs_list
    row_indices = []  # Creates empty list to append row indices of each value in obs_list
    col_indices = []  # Creates empty list to append col indices of each value in obs_list
    for m in obs_list:  # Iterates through ints in obs_list
        # Iterate through all values in obs_list and return the index values of where the values are located in the
        # Key Pad
        for n in range(0, 3):
            for o in range(0, 3):
                if m == key_pad2[o][n]:
                    row_indices.append(o)
                    col_indices.append(n)
        if m == 0:
            row_indices.append(3)
            col_indices.append(0)

    for x in range(len(obs_list)):
        temp_left = col_indices[x] - 1  # assigns test value for values to the left of current working index
        temp_right = col_indices[x] + 1  # assigns test value for values to the right of current working index
        temp_up = row_indices[x] - 1  # assigns test value for values above the current working index
        temp_down = row_indices[x] + 1  # assigns test value for values below the current working index
        # print("length: " +str(len(obs_list)))
        # print("x: " +str(x))
        # print(variations)
        # print("row index: " +str(row_indices[x]))
        # print("col index: " +str(col_indices[x]))
        # print("temps (r, l, u, d): " +str(temp_right)+str(temp_left)+str(temp_up)+str(temp_down))
        variations[x].append(key_pad2[row_indices[x]][col_indices[x]])  # appends current value to the corresponding list.
        # This section tests the directional temp values and appends them to the list if they're in the proper range.
        if 0 <= temp_left < len(key_pad2[row_indices[x]]):
            variations[x].append(key_pad2[row_indices[x]][col_indices[x]-1])
        if 0 <= temp_right < len(key_pad2[row_indices[x]]):
            variations[x].append(key_pad2[row_indices[x]][col_indices[x]+1])
        if 0 <= temp_up < len(key_pad2[row_indices[x]]):
            variations[x].append(key_pad2[row_indices[x]-1][col_indices[x]])
        if 0 <= temp_down < len(key_pad2[row_indices[x]]):
            variations[x].append(key_pad2[row_indices[x]+1][col_indices[x]])
        # Haven't figured out 8 and 0 relation yet due to the length of their corresponding key pad sub-list lengths
        if col_indices[x] == 1 and row_indices[x] == 2:
            variations[x].append(0)
        if col_indices[x] == 0 and row_indices[x] == 3:
            variations[x].append(8)

    output_list = list(itertools.product(*variations))  # This function iterates through all rows and returns the variations
    output_tup_str = [[str(i) for i in tup] for tup in output_list]
    output = [''.join(i) for i in output_tup_str]
    return output

observed = '123'
print(get_pins(observed))

# BETTER SOLUTIONS:

from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins2(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
