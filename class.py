#생성자를 알아봅시다
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def said(self, sentence):
        print(self.name, self.age, sentence)


    def getting_older(self):
        self.age += 1
        print("%s는 올해 %d 살이 되었다."%(self.name, self.age))
        return self.age #return 결과값

zuckerberg = Person("마크 저커버그", 37)
zuckerberg.said("결국에는 신념을 가진 자가 승리한다.")

steve_jobs = Person("엘론 머스크", 49)
steve_jobs.said("일주일에 80-100시간 가량 투자해야 한다.")
