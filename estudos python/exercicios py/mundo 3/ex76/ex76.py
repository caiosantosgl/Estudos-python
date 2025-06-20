produtos = ("Arroz", 5.49,
    "Feijão", 6.99,
    "Macarrão", 3.75,
    "Óleo", 7.20,
    "Açúcar", 4.10,
    "Café", 10.50,
    "Leite", 4.89,
    "Farinha", 3.20)
print('=' * 30)
print("PRODUTOS:")
print('=' * 30)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:-<30}', end="")
    else:
        print(f'R${produtos[c]:>6.2f}')
print('=' * 30)
