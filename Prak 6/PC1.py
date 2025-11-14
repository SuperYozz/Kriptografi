PC_1 = [ 
    57, 49, 41, 33, 25, 17, 9, 
    1, 58, 50, 42, 34, 26, 18, 
    10, 2, 59, 51, 43, 35, 27, 
    19, 11, 3, 60, 52, 44, 36, 
    63, 55, 47, 39, 31, 23, 15, 
    7, 62, 54, 46, 38, 30, 22, 
    14, 6, 61, 53, 45, 37, 29, 
    21, 13, 5, 28, 20, 12, 4 
] 
 
key_str = "0110110101100001011100100111010001101111000000000000000000000000" 
key_bits = [int(bit) for bit in key_str] 
permuted_key = [key_bits[pc - 1] for pc in PC_1] 
 
C0 = permuted_key[:28] 
D0 = permuted_key[28:] 
 
print("Kunci Awal:") 
for i in range(0, 64, 8): 
    print(' '.join(map(str, key_bits[i:i + 8]))) 
 
print("\nPermutasi PC-1 (Matriks 8x7):") 
for i in range(0, 56, 7): 
    print(' '.join(map(str, permuted_key[i:i + 7]))) 
 
print("\nC0:") 
for i in range(0, 28, 7): 
    print(' '.join(map(str, C0[i:i + 7]))) 
 
print("\nD0:") 
for i in range(0, 28, 7): 
    print(' '.join(map(str, D0[i:i + 7]))) 
