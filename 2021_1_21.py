#2021_01월 21일 배운 내용 코드--
import pandas as pd

### DataFrame
value = [ [23, "male", "seoul"], [26, "male", "busan"], [29, "female", "kyungki"],
          [20, "male", "daegu"]]
person = ["Andy", "Bob", "Carmen", "Dario"]
char = ["age", "gender", "area"]

person_data = pd.DataFrame(value, person, char)

## titanic_csv 생존자/사망자 불리언, 생존자, 사망자
titanic_csv = pd.read_csv("data/titanic.csv")

survived = titanic_csv["Survived"] == 1
survivor = titanic_csv[titanic_csv["Survived"] == 1]
the_dead = titanic_csv[titanic_csv["Survived"] == 0]
# print(survived)
# print(survivor)
# print(the_dead)

## titanic_csv 사람 수 구하기
titanic_csv = pd.read_csv("data/titanic.csv")

survivor = titanic_csv[titanic_csv["Survived"] == 1]
the_dead = titanic_csv[titanic_csv["Survived"] == 0]

# print("탑승한 사람 수 : ", titanic_csv["Survived"].size)
# print("생존한 사람 수 : ", survivor["Survived"].size)
# print("사망한 사람 수 : ", the_dead["Survived"].size)
#
# print("탑승한 사람 수 :", len(titanic_csv))
# print("탑승한 사람 수 :", len(survivor))
# print("탑승한 사람 수 :", len(the_dead))

# titanic_csv 사람 비율 구하기
titanic_csv = pd.read_csv("data/titanic.csv")

survivor = titanic_csv[titanic_csv["Survived"] == 1]
the_dead = titanic_csv[titanic_csv["Survived"] == 0]

# print("생존한 사람 수 / 탑승한 사람 수 : ", len(survivor), "/", len(titanic_csv))
# print("사망한 사람수 / 탑승한 사람 수 : ", len(the_dead), "/", len(titanic_csv))
#
# print("생존한 사람 수 백분율 : ", (len(survivor) / len(titanic_csv)) * 100)
# print("생존한 사람 수 백분율 : ", (len(the_dead) / len(titanic_csv) * 100))

## titanic_csv 요금별 생존자 분석
titanic_csv = pd.read_csv("data/titanic.csv")

under50_passenger = titanic_csv[titanic_csv["Fare"] < 50]
over50_passenger = titanic_csv[titanic_csv["Fare"] >= 50]

under50_passenger_alive = under50_passenger[under50_passenger["Survived"] == 1]
over50_passenger_alive = over50_passenger[over50_passenger["Survived"] == 1]

# print("탑승한 사람 수 : ", len(titanic_csv))
# print("$50미만 탑승자 수 :", len(under50_passenger))
# print("$50이상 탑승자 수 :", len(over50_passenger))

# print("$50미만 탑승자 수 / 전체 사람 수 :", (len(under50_passenger) / len(titanic_csv)) * 100)
# print("$50이상 탑승자 수 / 전체 사람 수 :", (len(over50_passenger) / len(titanic_csv)) * 100)

# print("$50미만 탑승자 중 생존자 수 :", len(under50_passenger_alive))
# print("$50미만 탑승자 중 생존자 수 비율 :", (len(under50_passenger_alive) / len(under50_passenger)) * 100)
# print("$50이상 탑승자 중 생존자 수 :", len(over50_passenger_alive))
# print("$50이상 탑승자 중 생존자 수 비율 :", (len(over50_passenger_alive) / len(over50_passenger)) * 100)

## 생존자와 사망자 막대 그래프

import pandas as pd
import matplotlib.pyplot as plt

titanic_csv = pd.read_csv("data/titanic.csv")

alive = titanic_csv[titanic_csv["Survived"] == 1]
dead = titanic_csv[titanic_csv["Survived"] == 0]

survivor = len(alive) / len(titanic_csv) * 100
the_dead = len(dead) / len(titanic_csv) * 100
print("생존한 사람 수 / 탑승한 사람 수 : ", len(alive), "/", len(titanic_csv))
print("사망한 사람수 / 탑승한 사람 수 : ", len(dead), "/", len(titanic_csv))
print("%0.2f%%" % survivor)
plt.bar(["alive", "dead"], height=[survivor, the_dead],
        color=["blue", "red"])
plt.text(0, survivor, "%0.2f%%" % survivor)
plt.text(1,  the_dead, "%0.2f%%" % the_dead)


print("{0}, {1}".format(survivor),'%')


plt.show()

