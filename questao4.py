nota1 = float(input("Qual a nota da primeira prova? "))
nota2 = float(input("Qual a nota da segunda prova? "))
nota3 = float(input("Qual a nota da terceira prova? "))

media1 = nota1 * 2
media2 = nota2 * 3
media3 = nota3 * 5
mediafinal = (media1 + media2 + media3) / 10
print("Sua média final é:", mediafinal)
if mediafinal >= 6:
    print("Você está aprovado")
else:
    print("Você foi reprovado")