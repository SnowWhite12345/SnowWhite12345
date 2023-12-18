usuario_web = ["André Perez", "andre.perez", "andre123", "andre.perez@gmail.com"]
print(usuario_web)
print(usuario_web[2])
print(type(usuario_web), "\n")

###################################################################################

idade = 20
saldo_em_conta = 723.15
usuario_loggedin = True

usuario_web = ["André Perez", idade, "andre.perez", "andre123", "andre.perez@gmail.com", saldo_em_conta, usuario_loggedin]

print(usuario_web)
print(usuario_web[6])
print(type(usuario_web), "\n")

#########################################################################################

fabricantes_mobile_china = ["Xiaomi", "Huawei"]
fabricantes_mobile_eua = ["Apple", "Motorola"]
fabricantes_mobile = fabricantes_mobile_china+fabricantes_mobile_eua
print(fabricantes_mobile_china)
print(fabricantes_mobile_eua)
print(fabricantes_mobile, "\n")

print(f"0: {fabricantes_mobile[0]}")
print(f"1: {fabricantes_mobile[1]}")
print(f"-1: {fabricantes_mobile[-1]}\n")

##########################################################################################

fabricantes_mobile_china = fabricantes_mobile[0:2]
fabricantes_mobile_eua = fabricantes_mobile[2:len(fabricantes_mobile)]

print("China: " + str(fabricantes_mobile_china))
print("EUA: " + str(fabricantes_mobile_eua), "\n")

##############################################################################################

fabricantes_mobile[2] = "Nokia"
print(fabricantes_mobile)