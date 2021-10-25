"""

    @author: Huy Nguyen
    - Just a tool to find a modular inverses pair!
    - The main function here is gen_inverse_pair().

    - After using gen_inverse_pair() to find a number that fit the size,
      you can try to get find its evenly divisible numbers.
      An example is val=7, size=1200, gen_inverse_pair() return 343, you can have a pair of <343,7> for public-secrety key pairs, and the modulo is the input size=1200.

"""


def is_prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
     
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0: return False
        return True
    else: return False


def is_validate_inverse_pair(x,y,size):
    for i in range(size):
        val = (i*x*y)%size
        if val != i:
            return False
    return True

# Generate pair value for <public key, private key> given size (number of maximum possibilities when encrypting encoded msg).
def gen_inverse_pair(val: int, size: int):
    for x in range(size):
        y=(val*x)%size
        if y == 1:
            if not is_prime(x):
                return x
            else:
                raise Exception('[Error] Cannot generate inverse pair with such given input value.')
    raise Exception('[Error] Cannot generate inverse pair with such given input value.')


if __name__ == "__main__":
    # Params
    val = 33
    size = 256

    out = gen_inverse_pair(val, size)
    print(out)
    assert(is_validate_inverse_pair(val,out,size))
