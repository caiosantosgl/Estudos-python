extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input("Escolha um número inteiro entra 0 e 20: "))
    if n >= 0 and n <= 20:
        break
    print("Número inválido, digite novamente.", end=" ")
print(f"O número que você digitou escrito por extenso é: {extenso[n]}")
