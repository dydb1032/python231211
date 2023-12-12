class Person:
    #초기화 루틴을 실행
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    def print(self):
        print(f"My name is {self.name}")

#2) 인스턴스(복사본)을 생성        
p1 = Person()
p2 = Person()
#3) 메서드 호출

Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)