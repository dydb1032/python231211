# 1) Connection클래스 : 주로 연결을 맺고, 트랜잭션 처리
# 2) Cursor클래스 : SQL구문을 실행하고, 결과셋을 처리
#
import sqlite3

#연결객체, 메모리에 임시 저장
con = sqlite3.connect(":memory:")
#커서 객체
cur = con.cursor()

#테이블 구조
cur.execute("CREATE table PhoneBook (Name text, PhoneNum text)")
#1건 입력
cur.execute("INSERT into PhoneBook values ('김길동', '010-111-1234')")

# 입력 파라메타 처리
name = '전우치'
phoneNumber = '010-22321-2314'
cur.execute("INSERT into PhoneBook values (?, ?)", (name, phoneNumber))

#다중의 레코드
datalist = (('강감찬', '010-333'),('박문수','010-456'))
cur.executemany("INSERT into PhoneBook values (?, ?)", datalist)

# #검색 구문
# cur.execute('SELECT * from PhoneBook')
# for row in cur:
#     print(row)


print('----fetchone()----')
print(cur.fetchone())

print('----fetchmany(2)----')
print(cur.fetchmany(2))

print('----fetchall()----')
print(cur.fetchall())

