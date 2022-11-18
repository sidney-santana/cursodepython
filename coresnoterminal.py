a = 3
b = 5
print('Os valores são \033[33m{}\033[m e \033[4;36m{}\033[m'.format(a, b))
nome = 'Sidney'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['pretobranco']))
