#sentence = input("enter a sentence: ")
#print('your sentence is: ' +sentence)
#word1 = input('enter word to replace: ')
#word2 = input('enter word to replace it with: ')
#print(sentence.replace(word1, word2))


#countries = ['united kingdom', 'ghana', 'nigeria', 'australia']
#print(countries[0][0])
#print(countries[0:3])

list1 = [1, 5, 10, 13, 6]
list2 = ['banana', 'apples', 'mango', 'oranges']
#list1.extend(list2)
list2.append('cherry')
#list2.clear()
list2.remove('banana')
print(list2.index('mango'))
list2.count('apples')
print(list1)
print(list2)
list1.sort()
print(list1)
list2.reverse()
list3 = list2.copy()
print(list3)
list2.pop()
list2.pop(1)
del list2[0]
del list2

#tuples
three_numbers = tuple((1, 'Home', True, 3))
#three_numbers = (1, 'Home', True, 3)

#functions
def greetings_function(name, age):
    print('welcome ' + name+ '. you are ' +str(age)+ ' years old.')
name = input('enter your name: ')
age = input('enter your age: ')
greetings_function(name, age)

#def greetings_function(*names):
#    print('welcome ' +names)
#greetings_function('john', 'tim', 'tom')

#return statements
def add_numbers(num1, num2):
    print('hello')
    return num1+num2

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
print(add_numbers(num1, num2))

#if statements
a = 2
b = 3
if a == b:
    print(str(a) + 'is greater than ' + str(b))

if a>b:
    print(str(a) +'is greater than ' + str(b)) 

if a < b:
    print(str(a) + 'is less than ' + str(b))

a = True
b = 'tim'
if a == True:
    print('a is True')
    