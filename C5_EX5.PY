#Conversion from kilograms to pounds andpounds to kilograms
print("{:13s}{}\t|\t{:13s}{}".format("Kilograms", "Pounds", "Pounds", "Kilograms"))
for i, j in zip(range(1, 200, 2), range(20, 516, 5)):
    print("{:.0f}{:20.1f}\t|\t{:.0f}{:20.2f}".format(i, i * 2.2, j, j * (1 / 2.2)))