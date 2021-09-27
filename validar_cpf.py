cpf_inicial = input('Digite o seu cpf: ')

cpf = cpf_inicial [:-2]
#print(cpf)

#digito10
soma = 0 
i = 0
for regressiva in range (10,1,-1) :
    
    a = int(cpf[i]) * regressiva
    soma = soma + int(a)
    i += 1

digito_10 = 11 - (soma % 11 )
if digito_10 > 9 :
    digito_10 = 0
else : 
    digito_10 = digito_10


cpf = f'{cpf}{digito_10}'
print(cpf)

#digito11
soma = 0 
i = 0
for regressiva in range (11,1,-1) :
    
    a = int(cpf[i]) * regressiva
    soma = soma + int(a)
    i += 1

digito_11 = 11 - (soma % 11 )
if digito_11 > 9 :
    digito_11 = 0
else : 
    digito_11 = digito_11


cpf = f'{cpf}{digito_11}'
print(cpf)

if cpf == cpf_inicial :
    print ('O cpf é válido!')

else:
    print ('Cpf inválido!')
