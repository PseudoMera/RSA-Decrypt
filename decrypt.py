import math

def binary_to_text(encrypted_list):
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

def primes_of_n(num, primes):
    for x in primes:
        for y in primes:
            if x * y == num:
                return (x,y)
    return -1

def mod_inverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def decrypt_result(nums):
    results = []
    for num in nums:
        results.append(pow(int(num), decryption_key, N))
    return results


def recipher_result(nums):
    results = []
    for num in nums:
        results.append(pow(num, E, N))
    return results

def decimal_to_chr(nums):
    message = ''
    for num in nums:
        message = message + chr(num)
    return message

#Message to be decrypted
binary_number = '00110100 00111001 00100000 00110001 00110000 00110111 00100000 00110100 00110110'
E = 13
N = 119

#Convert binary string to list
list_of_numbers = binary_number.split(' ')

#Decrypted numbers
numbers = binary_to_text(list_of_numbers)
print("Decrypted numbers: ", numbers)

#All primes from 2 to n
primes_less_than_n = sieve_of_eratosthenes(N)

#Two numbers that when multiplied equal N
P, Q = primes_of_n(N, primes_less_than_n)
print(f"Primes that compose N: {P} and {Q}")

#(P - 1) * (Q - 1)
PHI = (P - 1) * (Q - 1)
print("PHI: ", PHI)

#Key
decryption_key = mod_inverse(E, PHI)
print("Decryption key: ", decryption_key)

#Results
result = decrypt_result(numbers)
print("Result message: ", result)

#Recipher
recipher_numbers = recipher_result(result)
print("Recipher message: ", recipher_numbers)

#Final Text
message = decimal_to_chr(result)
print("Final message: ", message)