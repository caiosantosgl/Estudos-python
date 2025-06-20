tabela = 'flamengo', 'cruzeiro', 'bragantino', 'palemeiras', 'bahia', 'fluminense', 'atlético-MG', 'botafogo', 'mirassol', 'corinthians', 'grêmio', 'ceará SC', 'vasco da gama', 'são paulo', 'santos', 'EC vitória', 'internacional', 'fortaleza', 'juventude', 'sport Recife'
print(f'5 priméiros: {tabela[0:5]}')
print(f'Os 4 últimos{tabela[-4:]}')
print(f'Os times em odem alfabética: {sorted(tabela)}')
print(f'A posição do botafogo é: {tabela.index('botafogo')+1}.')
