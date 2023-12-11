print('-----튜플------')

tp = (10,20,30)
print(len(tp))

def calc(a,b):
    return a+b, a*b

result = calc(3,4)
print(result)

print("id:%s, name:%s" % ('kim', '김유신'))

print('\n-----set----')

a = {1,2,3,4}
b = {3,4,4,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print('\n---형식변환---')

a = list((1,2,3))
a.append(4)
print(a)

a = set(a)
print(a)

a = tuple(a)
print(a)

print('\n---dict---')
device = {'아이폰':5, "아이패드":10, "윈도우":20}
print(device)
print(device['아이폰'])

device['맥북'] = 15
device['아이폰'] = 6
print(device)

del device['아이폰']
print(device)

phone = {'kim':'111','lee':'222','park':333}
print('kim' in phone)
print('kang' in phone)

p = phone

p['kang'] = 123
print(p)
print(id(phone), id(p))


