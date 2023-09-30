#insira um numero na variável A e outro na variavél B
numA = float(input("Insira um numero: "))
numB = float(input("Insira um numero: "))
#Mostre em ordem descrente os dois numeros insiridos em cada variável
if numA >= numB:
    print(numA,numB)
else:
    print(numB, numA)