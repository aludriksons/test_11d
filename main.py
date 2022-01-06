mala=float(input("ievadi kvadrāta malas garumu virs 5: "))
if mala>=5:
  lauk=mala*mala
  lauk2=(mala+5)*(mala+5)
  print("procenti ir ",100*(lauk2/lauk),"%")
else:
  print("ievadīts nederīgs skaitlis")
