import math

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

def sieve_of_eratosthenes(limit):
    A = [True] * limit        
    A[0] = A[1] = False
    for (i, isprime) in enumerate(A):
        if isprime:
            for n in range (i * i, limit, i):
                A[n] = False 
    natural_numbers = [x for x in range(0, len(A) - 1) if A[x] is True]
    return natural_numbers


binary_number = '00110100 00111001 00100000 00110001 00110000 00110111 00100000 00110100 00110110'
e = 13
N = 119
list_of_numbers = binary_number.split(' ')
numbers = decimal_to_text(list_of_numbers)
res = sieve_of_eratosthenes(N)
print(res)
# num1 = ''.join(numbers[0:2])
# num2 = ''.join(numbers[2:5])
# num3 = ''.join(numbers[5:])

