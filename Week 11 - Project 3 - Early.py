from breezypythongui import EasyFrame

class TempConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Temperature Converter")
        self.addLabel(text = "Celcius",
                      row = 0, column = 0)
        self.getInputCelcius = self.addFloatField(value = 0.0,
                                                  row = 1,
                                                  column = 0)
        self.addLabel(text = "Fahrenheit",
                      row = 0, column = 1)
        self.getInputFahrenheit = self.addFloatField(value = 32.0,
                                                     row = 1,
                                                     column = 1)
        self.addButton(text = ">", row = 2, column = 0,
                       command = self.computeFahrenheit)
        self.addButton(text = "<", row = 2, column = 1,
                       command = self.computeCelcius)

    def computeFahrenheit(self):
        inputVal = self.getInputCelcius.getNumber()
        temp = 9.0/5.0 * inputVal + 32
        self.getInputFahrenheit.setValue(temp)

    def computeCelcius(self):
        inputVal = self.getInputFahrenheit.getNumber()
        temp = (inputVal - 32) * 5.0/9.0
        self.getInputCelcius.setValue(temp)

def main():
    TempConverter().mainloop()

if __name__ == "__main__":
    main()
