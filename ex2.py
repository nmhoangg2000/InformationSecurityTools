
      
  
def exponentiation(x, exp, N): 
    if (exp == 0): 
        return 1; 
    if (exp == 1): 
        return x % N; 
      
    t = exponentiation(x, int(exp / 2), N); 
    t = (t * t) % N; 
      
    
    if (exp % 2 == 0): 
        return t; 
          
    
    else: 
        return ((x % N) * t) % N; 
  

x = 692;
exp = 205; 
N = 731;  

mod = exponentiation(x, exp, N); 
print(mod); 



