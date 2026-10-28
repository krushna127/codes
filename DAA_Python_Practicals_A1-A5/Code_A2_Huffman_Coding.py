# Code-A2: Huffman Coding using Greedy Method
import heapq
from itertools import count

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char, self.freq = char, freq
        self.left, self.right = left, right

def print_codes(root, code=""):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(f"{root.char} : {code if code else '0'}")
        return
    print_codes(root.left, code + "0")
    print_codes(root.right, code + "1")

def huffman_encoding(chars, frequencies):
    if not chars or len(chars) != len(frequencies):
        raise ValueError("Provide matching, non-empty character and frequency lists.")
    if len(set(chars)) != len(chars):
        raise ValueError("Characters must be unique.")
    if any(f < 0 for f in frequencies):
        raise ValueError("Frequencies must be non-negative.")

    seq = count()
    heap = []
    for char, freq in zip(chars, frequencies):
        heapq.heappush(heap, (freq, next(seq), Node(char, freq)))

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        parent = Node(None, f1 + f2, left, right)
        heapq.heappush(heap, (parent.freq, next(seq), parent))

    print("\nHuffman Codes:")
    print_codes(heap[0][2])

def main():
    try:
        n = int(input("Enter number of characters: "))
        if n <= 0:
            print("Please enter at least one character.")
            return
        chars = input("Enter characters separated by spaces: ").split()
        if len(chars) != n or any(len(c) != 1 for c in chars):
            print(f"Enter exactly {n} single-character symbols.")
            return
        frequencies = list(map(int, input("Enter corresponding frequencies separated by spaces: ").split()))
        if len(frequencies) != n:
            print(f"Enter exactly {n} frequencies.")
            return
        huffman_encoding(chars, frequencies)
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
