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
 
shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1] 
 
C_values = [C0] 
D_values = [D0] 
 
for shift in shifts: 
    C_prev = C_values[-1] 
    D_prev = D_values[-1] 
     
    C_new = C_prev[shift:] + C_prev[:shift] 
    D_new = D_prev[shift:] + D_prev[:shift] 
     
    C_values.append(C_new) 
    D_values.append(D_new) 
 
# Display C and D values 
for i in range(17): 
    print(f"C{i}:", ' '.join(map(str, C_values[i]))) 
    print(f"D{i}:", ' '.join(map(str, D_values[i])))  