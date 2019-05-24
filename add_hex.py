def add_hex(A,B):
    
    key = "0123456789abcdef" #legit chars in hex base
    result = ""
    carry = ""

    while A != "" or B != "":
        
        if A == "":
            A = "0"
        elif B == "":
            B = "0"
            
        digit_a = str.index(key, A[-1]) #last char of A's index
        digit_b = str.index(key, B[-1]) #last char of B's index
        digit_c = str.index(key, carry)
        carry = "" #zero carry
        int_sum = (digit_a + digit_b + digit_c)
        
        if int_sum//16 != 0: #need to use carry
            hex_sum = str(int_sum//16) + key[int_sum%16]
            result = hex_sum[1] + result
            carry = hex_sum[0]
        else:
            hex_sum = key[int_sum%16]
            result = hex_sum + result
        A = A[:-1] #remove last char
        B = B[:-1] #remove last char
        
    if carry != "": #left carry
       result = carry + result
       
    return result
