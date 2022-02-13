#Financial applications: calculate tips
subtotal, gratuityRate = [float(x) for x in input("Enter the subottal and a grauity rate: ").split()]
gratuity = gratuityRate * subtotal / 100
total = subtotal +  gratuity
print("The gratuity is $", gratuity, " and total is ", total, "$")