from super_increasing_sequence import gen_super_increasing_sequence, \
        get_seq_available_size, \
        get_chosen_elements


# In case if you want to check the sequence having enough slot for possibilies.
desired_size = 101


# Private properties.
private_key = 23
private_modulo = 101
private_seq = gen_super_increasing_sequence(n=101)

# Public properties.
public_key = 22
public_seq = [(x*public_key)%private_modulo for x in private_seq]


assert(get_seq_available_size(public_seq) >= desired_size)


def encrypt(msg):  # Input as an encoded msg.
    return sum([public_seq[x] for x in msg])


def decrypt(x_sum):
    msg = set()
    orig_sum = (x_sum*private_key)%private_modulo
    eles = get_chosen_elements(private_seq, orig_sum)
    for val in eles:
        msg.add(val)
    return msg
