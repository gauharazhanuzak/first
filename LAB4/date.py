#1
import datetime

x = datetime.datetime.today()
y = datetime.timedelta(days = 5)

print(x - y)

#2
import datetime
x = datetime.date.today() - datetime.timedelta(days=1)
y = datetime.date.today()
z = datetime.date.today() + datetime.timedelta(days=1)
print(x)
print(y)
print(z)

#3
import datetime

x = datetime.datetime.today()

print(x.replace(microsecond=0))

#4
import datetime, math

print("The shape of input: yyyy/mm/dd")
x = str(input("The first date: "))
y = str(input("The second date: "))

day1 = datetime.datetime.strptime(x, "%Y/%m/%d")
day2 = datetime.datetime.strptime(y, "%Y/%m/%d")
deltaday = (day2 - day1)
deltasec = (day2 - day1) * 86400

print ("The days differences:", abs(deltaday.days))
print ("The second differences:", abs(deltasec.days))