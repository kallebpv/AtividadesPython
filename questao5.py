#Exercício 5
#Crie um programa no qual o usuário deverá inserir os valores da altura, largura
#e profundidade de uma caixa d’água, em cm. No final, exiba o volume dessa caixa d’água.
#Dica:
#Volume = Altura x Largura x Profundidade

altura= float(input("Me dê a altura: "))
largura= float(input("Me dê a largura: "))
profundidade= float(input("Me dê a profundidade: "))

volume = altura * largura * profundidade
#Conversão
volumefinal = volume/100
print("O volume da sua caixa d'Agua é ", volumefinal, "em metros cúbicos")