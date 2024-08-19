my_string= input ('Введите значение: ')
def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
print(findLen(my_string))
print('my_string' .upper())
print('my_string' .lower())
print('my_string' .replace(' ', ''))
name= 'my_string'
print(name[0])
print(name[-1])