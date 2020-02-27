def decimal_to_text(encrypted_list):
    numbers = []
    temp = ''
    for ch in encrypted_list:
        if(chr(int(ch,2)) != ' '):
            temp = temp + chr(int(ch,2))
            if(ch != encrypted_list[len(encrypted_list) - 1]):
                continue
        numbers.append(temp)
        temp = ''
    return numbers

def sieve_of_eratosthenes(n):
    crossed_numbers = {}
    natural_numbers = [x for x in range(2, n+1)]
    primes = []        
    return 0


binary_number = '00110100 00111001 00100000 00110001 00110000 00110111 00100000 00110100 00110110'
e = 13
N = 119
list_of_numbers = binary_number.split(' ')
numbers = decimal_to_text(list_of_numbers)

# num1 = ''.join(numbers[0:2])
# num2 = ''.join(numbers[2:5])
# num3 = ''.join(numbers[5:])

