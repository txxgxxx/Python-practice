#인스턴스의 나이를 높여봅시다.
class Person:
    name = ""
    age = 0

    def said(self, sentence):
        print(self.name, sentence)
        print(sentence, self.name)

    def getting_older(self):
        self.age += 1
        print("%s는 올해 %d 살이 되었다."%(self.name, self.age))
        return self.age #return 결과값

zuckerberg = Person()
zuckerberg.name = "마크 저커버그"
zuckerberg.age = 37
print(zuckerberg.name, zuckerberg.age)

zuckerberg.getting_older()

print(zuckerberg.name, zuckerberg.age)


elon_musk = Person()
elon_musk.name = "엘론 머스크"
elon_musk.age = 49
print(elon_musk.name, elon_musk.age)

elon_musk.getting_older()

print(elon_musk.name, elon_musk.age)

