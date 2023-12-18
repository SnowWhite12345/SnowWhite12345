# | = ou  / & = e / not = não

print(True | True)
print(True | False)
print(False | False)
print(False | True)
print("\n")

print(True & True)
print(True & False)
print(False & False)
print(False & True)
print("\n")

print(not True)
print(not False)
print("\n")

#==========================================================

idade = 19
tipo_sangue = "O-"
filhos = 0
telefone_fixo = None
telefone_fixo = ""

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(telefone_fixo))
print(bool(telefone_fixo))
print("\n")

#==========================================================

usuario_cadastro = "jose.santos"
senha_cadastro = "jsantos321"
usuario = "jose.santos"
senha = "jsantos123"

usuario_igual = usuario == usuario_cadastro
senha_igual = senha == senha_cadastro

print(usuario_igual)
print(senha_igual)

conceder_acesso = usuario_igual & senha_igual
print(conceder_acesso)