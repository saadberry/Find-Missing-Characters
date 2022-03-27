# program to compute the missing characters ( int + alphabets ) in a string 

def findMissingChar(s):
    
    digits = [0,1,2,3,4,5,6,7,8,9]
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x',
            'y','z']
   
   
    i = 0
    result=[]
    
    
    while i < len(digits):
        if str(digits[i]) not in s:
            result.append(i) 
        i+=1
            
    for i in alph:
        if i not in s:
            result.append(i) 
            
            
    print(result)
    

query = input('\n\nenter a string to find the missing characters: ')
print('\nthe missing characters are:\n')
findMissingChar(query)