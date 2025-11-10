from breezypythongui import EasyFrame

incDeduction = 15400
depDeduction = 300

class TaxCalc(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Tax Calculator")
        self.addLabel(text = "Income",
                      row = 0, column = 0)
        self.incomeField = self.addFloatField(value = 0.0,
                                              row = 0,
                                              column = 1)
        self.addLabel(text = "Dependents",
                      row = 1, column = 0)
        self.depField = self.addIntegerField(value = 0,
                                             row = 1,
                                             column = 1)
        self.addButton(text = "Compute", row = 2, column= 0,
                       columnspan = 2, command = self.computeTax)
        self.addLabel(text = "Total Tax",
                      row = 3, column = 0)
        self.taxField = self.addFloatField(value = 0.0,
                                           row = 3,
                                           column = 1,
                                           precision = 2)

    def computeTax(self):
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        tax = (income - incDeduction - numDependents * depDeduction) * 0.2
        self.taxField.setNumber(tax)

def main():
    TaxCalc().mainloop()

if __name__ == "__main__":
    main()
