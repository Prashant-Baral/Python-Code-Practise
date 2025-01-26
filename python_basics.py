num= int(input("Enter number: "))
if num % 2 ==0:
    print("Even")
elif num % 2 ==1:
    print("odd")


#haha
'''
Multi Line comment.
Code will print name.
'''

s="enter the no"\
    " of events"
print(s)


sa="23"
print(type(sa))
print(int(sa))
cnt=3.14
print(type(cnt))
lst=[1,2,3,4]
print(type(lst))

dct= {'key':'value'}
print(type(dct))
bool= True
print(type(bool))


#list starts with [] big brackets
# dictionary starts with {key: value} brackets with key and value






# gloabl and local variables

#local variables

a= "as i did"
def dingdong():
    a="as"
    print(a)

dingdong()
print(a)

# Global file

a= "as i did"
def dingdong():
    globala="as"
    print(a)

dingdong()
print(a)





c= 10 
print (c)
del c

g,h=10,23
g,h=h,g
print(g,h)

print(False==0)
print(True==1)
print(False==1)
print(True==0)

a= True+True+True-False-True
print(a)

a= True
b= False

print(a and b)
print(not b)
print(a or b)

'''
Operator Keywords: and, or, not, in, is
and Keyword – return ‘True’ if both the operands are ‘True’
or Keyword – return ‘True’ if at least one operand is ‘True’
'''
number= int(input("Enter a number "))
if(number<0):
    print("Negative")
elif(number>0):
    print("Positive")
else:
    print("Zero")

if(number in lst):
    print( "number is in lst")
elif(number not in lst):
    print("number not in lst")
    lst.append(number)
print(lst)

for i in lst:
    a=i+1
    print(a)

for i in range(0,100,9):
    print(i)

for i in range(5):
    if(i%2==0):
        continue
    print(i)


for i in range(0,20):
    if(i%2==0):
        continue
    print(i)
    if(i==15):
        break

for i in 'Prasiddhi':
    print(i)
    if(i=='h'):
        break

text='Prasiddhi'
for i, ch in enumerate(text):
    print(f"Index: {i} - Character: {ch}")



fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)

next_element = next(enum_fruits)
print(f"Next Element: {next_element}")


for i,j in enumerate('prasiddhi'):

    print(i,j)


print("python", end='@')
print('Geeks','for' ,'Geeks',sep='-')
name= "Prashant"
surname= " Baral"
print(f"my name is {name}{surname}")

in_num=1234
print("The sum is %d"%in_num)






x,y,z= input("Enter a number").split()
print(x)
print(y)
print(z)


