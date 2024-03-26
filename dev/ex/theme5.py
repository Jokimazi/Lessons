a = 4 # int
b = 3.4 # float
c = 'string'
d = True

l = [3, 5, 1, 5, 6, 1, 8, 9, 3] # list

print(l[2])

l.append(20)

print(l)

# l.insert(2, 'index 2')

print(l)

temp = l.copy()

temp.clear()
temp = []

print(temp)

print(l.count(3))

print(id(temp), id(l))

l.remove(3)
print(l)

l.reverse()

print(l)

l1 = [3, 1, 5, True]
l2 = ['sdfas', 2, 5]

l3 = l1 + l2
print(l3)

l3.extend(l2)
print(l3)

print(l)
l[1] = 10
print(l)

tup = (3, 1, 6, '2ds', True) # tuple
print(tup)

ind = tup.index(True)
print(ind)

s = {4, 2, 1, 5, 'sad', 3, 2} # set

s.add(12)
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s3 = s1.difference(s2)
print(s3)

s3 = s1.intersection(s2)
print(s3)

s3 = s1.union(s2)
print(s3)

s3 = s1.symmetric_difference(s2)
print(s3)

di = {'1': 'name1', '2': 'name2'} # dict

print(di['2'])

person = {
    'name': 'Андрей', 
    'age': 20, 
    'phone': '+79536424562', 
    'email': 'sda@gmail.com'
}

print(person['email'])

person['age'] = 23

print(person)

person['address'] = 'Адрес'

print(person)

items = person.items()

print(list(items)[0][1])

print(person.keys())
print(person.values())

names = ['Елизавета', 'Софья', 'Маргарита', 'Анастасия', 'Роман', 'Максим']

personas = {}

for index, name in enumerate(names):
    personas[str(index)] = name

print(personas)

for persona_id, persona_name in personas.items():
    print(f'id: {persona_id}')
    print(f'name: {persona_name}\n')


print(l)

m = 0

for i in l:
    if m < i:
        m = i

print(m)

print(len(personas))
print(sorted(l))

print(max(l), min(l))

