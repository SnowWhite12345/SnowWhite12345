from banco import Banco

conta1 = Banco(5458478, "Cleyton Farias", 380)

print(f"Número da conta: {conta1.numero}\nNome: {conta1.nome}\nSaldo: R${round(conta1.saldo,2)}\n")

conta1.alterarNome()
print(f"\nNome: {conta1.nome}\n")
conta1.depositar()

conta1.sacar()