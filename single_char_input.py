'''user_input= ''
while(True):
    user_input=input("Enter the input: ")
    if(len(user_input)==1):
        print(f"The entered character is {user_input}")
        break
    else:
        print("Please enter only a single character.") 

        '''

'''i=0
user_input=input("Enter the character:")[-1]
print(user_input)
print(user_input.center(10,'-'))
print(user_input.rjust(12,'.'))
'''

'''s='    GEEKS FOR GEEKS   '
print(s)
print(s[0])
print(s[-1])
print(s[-3])
print(s[3])

print(s[4:-1])
print(s[2:4])
print(s[-8:-1])
s="HA"+s[1:]
print(s)
print(s.strip())'''

a=[1,2,3,4,5,5,6,3,7]
b=[]
[b.append(val) for val in a if val not in b]
print(b)




