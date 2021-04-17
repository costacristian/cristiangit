
nome= input("informe seu nome: ")
peso= float( input("informe seu peso: "))
altura = float(input("informe sua altura: "))
alturaQuadrado=(altura*altura)
imc = peso/alturaQuadrado
print("{}seu IMC é {} e vc está muito bem".format(nome,imc))
