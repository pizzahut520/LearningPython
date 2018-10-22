a = 3
b = 'C:/xyu/source/repos/LearningPython/LearningPython/chapter1/variable.py'


print(b.split('/'))
print(b.replace('/', '\\'))

n = "something goes wrong"
print(b.strip('/'))

# content = input("enter something")
# url_path = "C:/xyu/source/repos/LearningPython/LearningPython/chapter1/{}".format(content)
# print(url_path)

def multistrings(a, b):
    print("function")
    return a*b

res = multistrings(a,b)
print(res)


def change_number(number):
    hidednumber = number.replace(number[3:7], '*'*4)
    return hidednumber

hidednumber = change_number('0668050586')
print(hidednumber)


for i in range(0,11):
    print(i)

    totototo