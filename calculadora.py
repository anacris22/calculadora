
print("calculadora")

 	 	
def somar(a,b):
	print("Soma")
	resultado = int(a) + int(b)
	return resultado
	
		
def menos(a,b):
	print("Menos")
	resultado = int(a) - int(b)
	return resultado

def multiplicacao(a,b):
	print("Multiplicao")
	resultado = int(a) * int(b)
	return resultado 
	
def divisao(a,b):
	print ("divisao")
	resultado = int(a) / int(b)
	return resultado

def operacaoValida(operacao):
	if operacao == "+":
		print ("somar")
		return True
	elif operacao == "-":
		print ("menos")
		return True
	elif operacao == "*":
		print("multiplicacao")
		return True
	elif operacao == "/":
		print("divisao")
		return True
	else:
		return False 

primeironumero = input ("digite o primeiro número: ")
print("digitado:",primeironumero)

operacao = input ("digite a operação: ")
print("operacao digitada",operacao)

segundonumero = input ("digite o segundo número:")
print ("digitado",segundonumero)

operacaoValida = operacaoValida(operacao)
print(operacaoValida)

if operacao == "+":	
	resultado = somar(primeironumero, segundonumero)
	print("resultado:", resultado)
elif operacao == "-":
	resultado = menos(primeironumero, segundonumero)
	print("resultado:", resultado)
elif operacao == "*":
	resultado = multiplicacao(primeironumero, segundonumero)
	print("resultado:", resultado)
elif operacao == "/":
	resultado = divisao(primeironumero,segundonumero)
	print("resultado:", resultado)