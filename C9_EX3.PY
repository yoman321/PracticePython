#Use the Date class
from datetime import date

time = 10000
for i in range(8):
    print(date.fromtimestamp(time / 1000))
    time *= 10