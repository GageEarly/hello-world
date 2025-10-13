annualRate = .12
monthlyRate = annualRate / 12

purchasePrice = float(input("Enter the purchase price: $"))
downPayment = purchasePrice * 0.1
purchasePrice = purchasePrice - downPayment
monthlyPayment = .05 * purchasePrice
month = 1
balance = purchasePrice
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
while balance > 0:
   if monthlyPayment > balance:
       monthlyPayment = balance
       interest = 0
   else:
       interest = balance * monthlyPayment
   principal = monthlyPayment - interest
   remaining = balance - monthlyPayment
   print("%2d%15.2f%15.2f%17.2f%17.2f%17.2f" % (month, balance, interest, principal, monthlyPayment, remaining))
   balance = remaining
   month += 1
