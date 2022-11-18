
nome = str(input('Qual é seu nome? '))
if nome == 'João':
    print('Que nome \033[36mB\033[35mO\033[34mN\033[33mI\033[32mT\033[31mO\033[m!')
    print('Tenha um bom dia {}{}'.format(nome, ' <3'))
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular heim {}!'.format(nome))
elif nome in 'Marcos Ana Bia ':
    print('Que belo nome...')
else:
    print('Seu nome é bem normal.')
    print('Tenha um bom dia {}'.format(nome))

idade = int(input('Mais uma coisa ... Quantos anos você tem {}?'.format(nome)))
if idade > 0 or idade < 10:
    print('Que nenêzinho ...')
elif idade > 10 or idade < 25:
    print('IHHHH Aborrecente! ')
else:
    print('Que idoso!')

nf = int(input('Uma última coisa de extrema importância ... Qual seu número da sorte?'))
if nf == 13:
    print('\033[31;42mVocê ganhou!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
else:
    print('Que tipo de lunático tem número da sorte?!')