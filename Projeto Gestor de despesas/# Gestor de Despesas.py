# Gestor de Despesas
print("== GESTOR DE DESPESAS ==")

# Lista para armazenar despesas
despesas = []

# Pergunta ao usuário quantas despesas ele tem
num_despesas = int(input("Digite quantas despesas você tem: "))

# Loop para armazenar despesas
for i in range(1, num_despesas + 1):
    valor = float(input(f"Digite o valor da despesa {i} em R$: "))
    despesas.append(valor)

    # Perguntar se tem mais despesas
    continuar = input("Você tem mais despesas? [Digite sim/não]: ").strip().lower()
    if continuar == "não":
        break

# Pergunta o salário e saldo atual
salario = float(input("\nDigite o valor do seu salário em R$: "))
saldo = float(input("Você possui saldo? Insira o saldo atual em R$: "))

# Calcula os totais
total_despesas = sum(despesas)
saldo_final = (salario + saldo) - total_despesas

# Exibe o balanço comercial
print("\n=== BALANÇO COMERCIAL ===")
print(f"Total de despesas: R$ {total_despesas:.2f}")
print(f"Saldo após pagar despesas: R$ {saldo_final:.2f}")

if saldo_final > 0:
    saldo_anual = saldo_final * 12
    print(f"Se guardar esse saldo todo mês, terá R$ {saldo_anual:.2f} em 1 ano! 💰")
else:
    print("Atenção! Suas despesas são maiores que sua renda. ⚠️")

print("================================")
