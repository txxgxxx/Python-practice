 #상속을 알아봅시다.
 #class 자식 클래스명(부모 클래스):
#클래스 옆에 부모 클래스를 적으면 부모 클래스의 상태와 행위를 상속받는다.
#자식 클래스에 함수를 사용하여 self 매개변수를 활용할 수 있다.
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

class Founder(Person):

    def establish(self, enterprise):
        print(self.name, enterprise)

zuckerberg = Founder("마크 저커버그", 37)
zuckerberg.establish("facebook")
steve_jobs = Founder("스티브 잡스", 54)
steve_jobs.establish("apple")
