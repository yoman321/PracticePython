#The Stock class
class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice
    
    def getChangePercent(self):
        if (self.previousClosingPrice > self.currentPrice):
            return -100 + (self.currentPrice / self.previousClosingPrice * 100)
        else:
            return 100 - (self.previousClosingPrice / self.currentPrice * 100)
    
stock = Stock("ORCL", "Oracle Corporation", 34.5, 34.35)
print("The price change for {} is {:.2f}%.".format(stock.name, stock.getChangePercent()))