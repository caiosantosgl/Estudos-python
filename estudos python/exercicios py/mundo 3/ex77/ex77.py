palavras = ("python", "banana", "carro", "felicidade", "livro", "teclado", "janela", "programacao", "viagem", "oceano")
for i in palavras:
    print(f'\nNa palavra {i} existe as vogais: ', end="")
    for l in i:
        if l.lower() in 'aeiou':
            print(l, end=" ")
