from hashlib import sha1 as h
from os.path import getsize
from os.path import isfile
from collections import deque


"""

    @author: Huy Nguyen
    Just a basic implementation for Merkle Tree (Hash Tree) for a given input file.
    Using SHA1 for crypto hash algorithm.

"""


def bitwise_or_bytes(a, b):
    int_rs = int.from_bytes(a, byteorder='big') | int.from_bytes(b, byteorder='big')
    return int_rs.to_bytes(max(len(a), len(b)), byteorder='big')


class MerkleNode(object):
    def __init__(self, hash_val):
        self.hash_val = hash_val


class MerkleLeafNode(MerkleNode):
    def __init__(self, data):
        super().__init__(h(data))


class MerkleNonleafNode(MerkleNode):
    def __init__(self, data1, data2):
        super().__init__(h(bitwise_or_bytes(data1.hash_val.digest(), data2.hash_val.digest())))
        self.left = data1
        self.right = data2


def get_merkle_tree_file_hash(file_path, block_size=4):
    assert isfile(file_path), '[Error] Invalid input file path.'

    file_size = getsize(file_path)
    print('File size: %d bytes.' % file_size)
    print('Block size: %d bytes.' % block_size)

    assert file_size >= block_size, '[Error] Block size cannot be larger than file size.'

    with open(file_path, 'rb') as file:
        num_blocks = int(file_size/block_size)
        redundant = file_size%block_size

        if redundant != 0:
            num_blocks += 1

        my_queue = deque()  # Used for Leveling Traverse.

        # Hash leaf nodes.
        for i in range(num_blocks):
            data_block = file.read(block_size)
            node = MerkleLeafNode(data_block)
            my_queue.append(node)

        # Hash all non-leaf nodes and get the result.
        while len(my_queue) > 1:
            size = int(len(my_queue)/2)
            for i in range(size):
                node1 = my_queue.popleft()
                node2 = my_queue.popleft()
                if node2 is not None:
                    node = MerkleNonleafNode(node1, node2)
                    my_queue.append(node)
                else:
                    my_queue.append(node)

        return my_queue.popleft()


def main():
    file_path = './my_file.txt'
    root_node = get_merkle_tree_file_hash(file_path, block_size=4)
    print('Result root hash: ', root_node.hash_val.digest())

if __name__ == "__main__":
    main()
