import heapq as hq
from dataclasses import dataclass, field
from typing import Any
from BitVector.BitVector import BitVector


@dataclass(order=True)
class HuffmanNode:
    priority: int
    item: Any = field(compare=False)

    def __str__(self):
        return f"({self.priority}, {self.item.__repr__()})"

    __repr__ = __str__


@dataclass
class EncodedData:
    data: str
    table: dict
    tree: HuffmanNode


# Create a table of frequencies for all items in iterable
def frequencies(iterable):
    freq_table = {}
    for elem in iterable:
        if elem in freq_table:
            freq_table[elem] += 1
        else:
            freq_table[elem] = 1
    return freq_table


# Build a huffman tree
# All leaves are characters
def huffman_tree(frequencies):
    heap = []
    # Build a priority queue of characters and their frequencies
    for key, frequency in frequencies.items():
        hq.heappush(heap, HuffmanNode(priority=frequency, item=key))

    # Algorithm:
    # Take 2 smallest elements
    # Create new node with added frequency (priority)
    # Add to heap
    # Repeat until there is only one node left, which is now the root
    while len(heap) > 1:
        a = hq.heappop(heap)
        b = hq.heappop(heap)
        new_node = HuffmanNode(priority=a.priority + b.priority, item=(a, b))
        hq.heappush(heap, new_node)

    # heap[0] is the root node
    return heap[0]


# Create a translation table for symbols to codes
def translation_table(huffman_tree):
    if isinstance(huffman_tree.item, str):
        return {huffman_tree.item: [1]}

    def node_table_r(node, path_so_far):
        item = node.item
        if isinstance(item, str):
            return {item: path_so_far}
        elif isinstance(item, tuple) and len(item) == 2:
            left, right = item
            left = node_table_r(left, path_so_far + [0])
            right = node_table_r(right, path_so_far + [1])
            return {**left, **right}
        else:
            raise Exception("Internal error: item is not valid")

    return node_table_r(huffman_tree, [])


# Encode a raw stream of data
def encode(raw_data):
    freqs = frequencies(raw_data)
    htree = huffman_tree(freqs)
    table = translation_table(htree)
    bitdata = [bit for bits in map(
        lambda x: table[x], raw_data) for bit in bits]
    return EncodedData(data=bitdata, table=table, tree=htree)


# Decode an encoded data stream
def decode(encoded_data):
    tree = encoded_data.tree
    data = encoded_data.data
    raise NotImplementedError()
