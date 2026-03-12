try:
  x = int(input("Num1 :"))
  y = int(input("Num2 :"))
  z = x / y
  print(z)

except ZeroDivisionError as e:
  print("Div by zero :", e)

except Exception as e:
  print("Error :", e)

finally:
  print("Hello End")