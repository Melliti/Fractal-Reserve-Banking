import sys
import csv

class Main:
    rows = []
    moneyCreated = {}

    def moneySupply(self, idx, year): 
        r = 0
        sum = 0
        if (idx < len(self.rows[0])):
            for row in self.rows:
                if (r != 0):
                    sum += int(row[idx])
                r += 1
            # print(sum)
            # print(self.moneyCreated[" Deposits " + str(year)])
            print (sum + self.moneyCreated[" Deposits " + str(year)])
            self.moneySupply(idx + 1, year - 1)


    def rowsToBankDeposits(self, idx):
        r = 0
        sum = 0
        if (idx < len(self.rows[0])):
            for row in self.rows:
                if (r != 0):
                    sum += int(row[idx])
                r += 1
            self.moneyCreated[self.rows[0][idx]] = sum * (1 / (1 - (10/100))) / (10/100)
            self.rowsToBankDeposits(idx + 1)
            

    def start(self):
        with open(sys.argv[1], 'r') as csvFile:
            datas = csv.reader(csvFile, delimiter=",")
            for row in datas:
                self.rows.append(row)
        # print (self.rows)
        self.rowsToBankDeposits(1)
        # print("MS")
        self.moneySupply(1, 2018)
        # print(self.moneyCreated)

main = Main()
if (len(sys.argv) == 2):
    main.start()
