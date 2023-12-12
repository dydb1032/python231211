#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수로 리스트를 저장
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result
    
print(intersect("HAM", "SPAM"))

x = 10
def func1(a):
    return a + x

print(func1(1))

def func2(a):
    x = 5
    return a + x

print(x)
print(func2(1))

def union(*ar):  ## 가변 파라미터 별 하나는 튜플, 두개는 리스트

    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)

    return result

print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))

## lambda 입력 : <처리>
## g = lambda x,y : x*y

