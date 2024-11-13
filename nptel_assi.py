def intreverse(n):
  rem = 0
  rev = 0
  size = len(str(n))
  
  if (size == 1):
    print(n)
    return n
  
  else:
    for i in range(0, size):
      rem = n % 10
        #   print (rem)
        #   print(" ")
      rev = (rev * 10) + rem
      n = n // 10
      
      
  print (rev)
  print(" ")
      
  return rev
  
  	
intreverse(368)
	
intreverse(798798)

intreverse(7)

def intreverse(n):
  rem = 0
  rev = 0
  size = len(str(n))
  
  if (size == 1):
    print(n)
    return n
  
  else:
    for i in range(0, size):
      rem = n % 10
        #   print (rem)
        #   print(" ")
      rev = (rev * 10) + rem
      n = n // 10
      
  return rev
  
  
  
  
  
  
def matched(s):
    char_count = []
    for i in stri:
        char_count.append(i)
    
    if len(char_count) == 0:
        return True


#second pro

def matched(s):
    char_count = []
    for i in s:
        if (i == '('):
            char_count.append(i)
        elif (i == ')'):
            char_count.append(i)
    
    if len(char_count) == 0:
        return True
        
    else:
        open_count = 0
        close_count = 0
        
        for i in char_count:
            if (i == '('):
                open_count+=1
        
            elif (i == ')'):
                close_count+=1
                
        if (open_count == close_count):
                return True
                
        else:
            return False
            
def matchi(s):
    Update_lst = list(s)
    
    for i in range (len(Update_lst)):
        if Update_lst[i] == "(":
            if ')' in Update_lst[i+1:]:
                Update_lst[Update_lst.index(')')] = '$'
    
    print(Update_lst.count('$') == Update_lst.count('('))            
    return (Update_lst.count('$') == Update_lst.count('('))
    
matchi("((jkl)78(A)&l(8(dd(FJI:),):)?)")

def matchwed(s):
    char_count = []
    for i in s:
        if (i == '('):
            char_count.append(i)
        elif (i == ')'):
            char_count.append(i)
    
    if len(char_count) == 0:
        return True
        
    else:
        open_count = 0
        close_count = 0
        
        for i in char_count:
            if (i == '('):
                open_count+=1
        
            elif (i == ')'):
                close_count+=1
                
        if (open_count % 2 == 0):
            if (close_count % 2 == 0):
                return True
                
            else:
                return False
                
        else:
            return False
            
#2nddd
def matched(s):
    char_count = []
    for i in s:
        if (i == '('):
            char_count.append(i)
        elif (i == ')'):
            char_count.append(i)
    
    if len(char_count) == 0:
        return True
        
    else:
        open_count = 0
        close_count = 0
        
        for i in char_count:
            if (i == '('):
                open_count+=1
        
            elif (i == ')'):
                close_count+=1
                
        if (open_count == close_count):
                return True
                
        else:
            return False
        

#3rd pro

# if num > 1:
  
#     for i in range(2, (num//2)+1):
      
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


def check_prime(num):
    if num > 1:
        for i in range(2, (num//2) + 1):
            if (num % i == 0):
                return False
            
        else:
            print("not prime")
            return True
            
    else:    
        return False


def sumprimes(l):
    prime_sum = 0
    for i in l:
        if check_prime(i):
            prime_sum+=i
            
    print(prime_sum)
    return prime_sum


	
sumprimes([4,6,15,27])
print(' ')

sumprimes([-3,-5,3,5])


