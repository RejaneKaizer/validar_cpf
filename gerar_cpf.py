from random import randint
numero = str (randint (000000000, 999999999))
print(numero)
cpf_inicial = numero
#print(cpf)

#digito10
soma = 0 
i = 0
for regressiva in range (10,1,-1) :
    
    a = int(cpf_inicial[i]) * regressiva
    soma = soma + int(a)
    i += 1

digito_10 = 11 - (soma % 11 )
if digito_10 > 9 :
    digito_10 = 0
else : 
    digito_10 = digito_10


cpf_final = f'{cpf_inicial}{digito_10}'
print(cpf_final)

#digito11
soma = 0 
i = 0
for regressiva in range (11,1,-1) :
    
    a = int(cpf_final[i]) * regressiva
    soma = soma + int(a)
    i += 1

digito_11 = 11 - (soma % 11 )
if digito_11 > 9 :
    digito_11 = 0
else : 
    digito_11 = digito_11


cpf_final = f'{cpf_final}{digito_11}'
print(cpf_final)

