list = ['peter', 'lilei', 'wangwu', 'xiaoming']

#print(list[2])
#print(list[2:])
"""
list2 = [
    1,
    1.1,
    'string',
    print(1),
    True,
    [1,2],
    (1,2),
    {"key", "value"}

]

print(list2)"""

"""
names = ["xinchen", "jingjing", "Elynn", "titi"]
ages = [34, 33, 3, 5]
for name, age in zip(names, ages):
    print(name, age)


urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0'.format(number)
        for number in range(1,14)]
for url in urls:
    print(url)


user_info = {
    'name': 'xiapming',
    'age': '23',
    'sex': 'male'
}
print(user_info)
"""

"""
tuple = (1, 2, 3)
print(tuple)

list = ["Elynn", "jingjing", "Elynn"]
set = set(list)
print(set)
"""

file_name = "C:/xyu/source/repos/LearningPython/LearningPython/chapter1/variable.py"

f = open(file_name, 'r')
content = f.read()
print(content)

f.close


