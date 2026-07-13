with open("motto.txt", "x") as file:
  file.writelines("Fiat Lux!\n")
with open("motto.txt", "r") as file:
  print(file.read())
with open("motto.txt", "a") as file:
  file.writelines("Let there be light!")