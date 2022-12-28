def get_bytes(the_char):
    return ord(the_char)


def get_char(the_bytes):
    return chr(the_bytes)


def sum_code_points():
    first = input()
    second = input()
    the_sum = ord(first) + ord(second)
    print(the_sum)


def construct_unicode():
    first = int(input())
    second = int(input())
    third = int(input())
    fourth = int(input())
    print(f'{chr(first)}{chr(second)}{chr(third)}{chr(fourth)}')


def get_last_byte():
    text = input()
    the_bytes = text.encode()
    print(the_bytes[-1])


if __name__ == '__main__':
    print(get_bytes('a'))
    print(get_char(97))
    print(get_char(get_bytes('a')))

    first_bytes = b'123'
    print(first_bytes)
    print(first_bytes[0])  # 49
    print(first_bytes[1])  # 50
    print(first_bytes[2])  # 51

    print(get_char(first_bytes[0]))
    print(get_char(first_bytes[1]))
    print(get_char(first_bytes[2]))

    # sum_code_points()
    # construct_unicode()

    # print(bytes([31]))
    # print(bytes([32]))
    # print(bytes([126]))
    # print(bytes([127]))
    # array = bytes([31, 32, 126, 127])
    # print(array)

    # encoding
    strange = b'\xdb\xf1\xef\xe7\xf8d\xea'
    strange2 = bytes('Ûñïçødê', encoding='utf-8')
    print(strange)
    print(strange2)
    strange_array = ['\xdb', '\xf1', '\xef', '\xe7', '\xf8', 'd', '\xea']
    print(''.join([get_char(get_bytes(char)) for char in strange_array]))
    print(strange2.decode('utf-8'))

    chinese_hello = bytes('你好，世界', encoding='utf-8')
    chinese_hello_enc = '你好，世界'.encode('utf-8')
    print(f'chinese_hello:{chinese_hello}; chinese_hello_enc:{chinese_hello_enc}')
    print(chinese_hello.decode("utf-8"))

    # to_bytes()
    print((100).to_bytes(1, byteorder='little'))  # b'd'
    # print((100).to_bytes(2, byteorder='little'))

    second_number = (1024).to_bytes(2, byteorder='little')
    print(second_number)  # b'\x00\x04'

    third_number = (1024).to_bytes(2, byteorder='big')
    print(third_number)  # b'\x04\x00'

    # decoding
    bye_bytes = b'bye bytes'
    hello_str = str(bye_bytes, encoding='utf-8')
    hello_another_str = bye_bytes.decode()
    # print(hello_str == hello_another_str)  # True
    print(hello_another_str)

    # from_bytes()
    int_to_bytes = (1024).to_bytes(2, 'little')
    print(int_to_bytes)  # b'\x00\x04'

    bytes_to_int = int.from_bytes(int_to_bytes, 'little')
    print(bytes_to_int)  # 1024

    # get last byte from input
    #get_last_byte()


