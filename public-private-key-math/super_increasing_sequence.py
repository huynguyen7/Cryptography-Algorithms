'''

    A super-increasing-sequence is a list of numbers that their sum from given index i to j are always UNIQUE.
    In another word, the uniqueness of each sum is guaranteed.
    
    +Source: https://en.wikipedia.org/wiki/Superincreasing_sequence

'''


def is_super_increasing_sequence(seq: list):
    seq_sum = 0
    flag = True
    for n in seq:
        if n <= seq_sum:
            flag = False
            break
        seq_sum += n
    return flag 


# Generating list of super increasing sequence with given size n.
def gen_super_increasing_sequence(init_seq=[1,3,5], n=1):
    assert isinstance(n, int) and n >= 0, '[Error] Invalid size n for super-increasing-sequence.'

    seq = init_seq if init_seq is not None else [1,3,5]
    #seq = [1,3,6]
    for i in range(n):
        seq_sum = sum(seq)
        seq.append(seq_sum+1)
    return seq[:n] if len(seq) > n else seq


# Just a binary search for equal or greatest (less than) key value.
def bin_less(arr, val):
    if len(arr) == 0:
        raise Exception('[Error] Empty array.')

    low = 0
    high = len(arr)-1

    while(low <= high):
        mid = int(low+(high-low)/2)
        if arr[mid] == val: return mid
        elif arr[mid] < val: low = mid+1
        else: high = mid-1
    return high


# Validate chosen sum.
def get_chosen_elements(seq: list, chosen_sum: int):
    chosen_elements = set()
    visited = set()

    while True:
        idx = bin_less(seq, chosen_sum)
        chosen_sum -= seq[idx]
        #chosen_elements.append(seq[idx])
        chosen_elements.add(idx)
        if chosen_sum < 0 or idx in visited:
            print(chosen_sum)
        elif chosen_sum == 0:
            break
        visited.add(idx)

    if len(chosen_elements) == 0 or chosen_sum != 0:
        raise Exception('[Error] Invalid chosen sum.')
    return chosen_elements

'''
    Get the available size of a sequence. Sometimes, you may have a zeros public_seq..
    Just to make sure, if you plan to have 256 possibilities, please use modular_inverses with size more than 256 and use this function for sanity check.
'''
def get_seq_available_size(seq):
    for i in seq:
        if seq[i] == 0:
            return i+1
    return len(seq)
