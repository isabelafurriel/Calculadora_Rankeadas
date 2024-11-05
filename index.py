# Função que calcula o saldo de vitórias e determina o nível do jogador
def calcular_rank(v, d):
# Calcular o saldo de vitórias
    saldo_v = v - d

    if v < 10:
        nivel = "Ferro"
    elif 11 <= v <= 20:
        nivel = "Bronze"
    elif 21 <= v <= 50:
        nivel = "Prata"
    elif 51 <= v <= 80:
        nivel = "Ouro"
    elif 81 <= v <= 90:
        nivel = "Diamante"
    elif 91 <= v<= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

# Retorna o saldo de vitórias e o nível
    return saldo_v, nivel

v = int(input("Informe a quantidade de vitórias: "))
d = int(input("Informe a quantidade de derrotas: "))
# Calcular o saldo e o nível
saldo_v, nivel = calcular_rank(v, d)

print(f"O Herói tem de saldo de {saldo_v} está no nível de {nivel}")
