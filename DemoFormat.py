#문자열 연결
url = "http://www.multi.com/?page=" + str(1)
print(url)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(5))

print(f"{10:x}")
print(f"{10:b}")
print(f"{4/3:e}")
print(f"{4/3:f}")
print(f"{4/3:.2f}")
print(f"{1500000:,}")

#파일 쓰기
#raw string notation(가공하지 않은 표기)
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기
print("---파일 읽기---")
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)

#처음으로 돌아가
f.seek(0)

print(f.readline(), end = "")
print(f.readline(), end = "")
f.seek(0)

result  = f.readlines()
for item in result:
    print(item, end="")

f.close()
