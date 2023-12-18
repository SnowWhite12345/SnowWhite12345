# Concatenação
nome = "Andre Marcos"
sobrenome = "Perez"

apresentação = "Olá, meu nome é " + nome + " " + sobrenome + "."
print(apresentação)
#=====================================================================
nome = "Andre Marcos"
sobrenome = "Perez"

apresentação = f"Olá, meu nome é {nome}, {sobrenome}."
print (apresentação)

#=====================================================================
#Fatiamento fixo

email = "vargasandressa65@gmail.com"

print("0: " + email[0])
print("11: " + email [11])

print("-1: " + email [-1])
print("-2: " + email [-2])
#======================================================================
# Fatiamento por intervalo

email_usuario = email[0:11]
print (email_usuario)

#======================================================================
email_provedor = email[12:21]
print(email_provedor)

#=======================================================================
#metodos

endereco = "Avenida Paulista, 1811, São Paulo, São Paulo, Brasil"
#maiúsculo: string.upper()
print(endereco.upper())

#posicao: string.find(substring)
posicao = endereco.find("Brasil")
print(posicao)

#substituição: string.replace(antigo,novo)
print(endereco.replace("Avenida", "Av."))

#===========================================================================
#Conversão

idade = 19
print(type(idade))

idade = str(56)
print(idade)
print(type(idade))

#==========================================================================
faturamento = "R$ 35 mi"
print (faturamento)
print (type(idade))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))

#==========================================================================
latlon = "-29.40093;-10.504932"
posicao_char_divisao = latlon.find(";")
print(posicao_char_divisao)

lat_startup = latlon[0:posicao_char_divisao]
print(lat_startup)

lon_startup = latlon[posicao_char_divisao+1:len(latlon)]
print(lon_startup)