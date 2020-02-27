def decimal_to_text(encrypted_list):
    numbers = []
    for ch in encrypted_list:
        if(chr(int(ch,2)) != ' '):
            numbers.append(chr(int(ch,2)))
    return numbers

binary_number = '00110100 00111001 00100000 00110001 00110000 00110111 00100000 00110100 00110110'
list_of_numbers = binary_number.split(' ')

numbers = decimal_to_text(list_of_numbers)
num1 = ''.join(numbers[0:2])
num2 = ''.join(numbers[2:5])
num3 = ''.join(numbers[5:])

