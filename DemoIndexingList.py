# DemoIndexingList.py

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))

print(strA[0:3])
print(strB[0:6])
print(strB[-3:])
print(strB[-8:])

print("---리스트---")
colors = ['red','blue','green']

print(len(colors))

colors.append('white')
colors.extend(['red','yellow','pink'])

print(colors)
colors.sort()
print(colors)
colors.remove('blue')
print(colors)

#반복구문
#디버깅할 때 중단점(break point)
for item in colors:
    print(item)

### 튜플이 주로 사용되는 경우 1. 함수에서 하나 이상 리턴, 2. 