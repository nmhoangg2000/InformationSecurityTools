# Python 3 program to find modular 
# inverse of a under modulo m 
  
# A naive method to find modulor 
# multiplicative inverse of 'a' 
# under modulo 'm' 
  
def modInverse(a, m): 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1): 
        return 0
  
    while (a > 1): 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
    # Make x positive 
    if (x < 0): 
        x = x + m0 
  
    return x 
  
  
# Driver code 
a = 25
m = 58
  
# Function call 
print("Modular multiplicative inverse is", 
      modInverse(a, m)) 