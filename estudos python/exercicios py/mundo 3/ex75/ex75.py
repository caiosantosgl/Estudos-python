v = int(input("Digite um número inteiro: ")), int(input("Digite outro número inteiro: ")), int(input("Digite outro número inteiro: ")), int(input("Digite outro número inteiro: "))
print(f"O número 9 apareceu {v.count(9)} vezes.")
if 3 in v:
    print(f"O primeiro número 3 foi digitado na posição: {v.index(3)+1}")
else:
    print("O número 3 foi digitado 0 vezes.")
print(f"Os números pares foram: ", end='')
for c in v:
    if c % 2 == 0:
        print(c, end=' ')