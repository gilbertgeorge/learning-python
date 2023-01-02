character_value = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                   'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                   'X': 24, 'Y': 25, 'Z': 26}


def poly_hash(string_to_hash, a, m):
    hash_value = 0
    for i, char in enumerate(string_to_hash):
        hash_value += character_value[char] * a ** i
    return hash_value % m


if __name__ == '__main__':
    print(poly_hash('BBAB', 3, 11))
    print(poly_hash('ABCC', 3, 11))
    print()
    print(poly_hash('AAAA', 3, 13))
    print(poly_hash('EBCB', 3, 13))
    print()
    print(poly_hash('CCDB', 3, 13))
    print(poly_hash('ACCD', 3, 13))

