class employee:
    Ecode=None
    Ename=None
    Monthlysal=None
    def accept(self):
        self.Ecode=int(input("Ecode"))
        self.Ename=input("Ename")
        self.Monthlysal=int(input("Monthlysal"))
    def calcsal(self):
        self.yearlysal=self.Monthlysal*12
    def display(self):
        print(self.Ecode)
        print(self.Ename)
        print(self.Monthlysal)
        print(self.yearlysal)
E1=employee()
E1.accept()
E1.calcsal()
E1.display()



