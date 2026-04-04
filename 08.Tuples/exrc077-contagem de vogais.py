palavras =  ('Estudar', 'Python', 'Programação', 'Linux',
             'Git', 'GitHub', 'Pycharm')
for palavra in palavras:
    print(f'\n Na palavra {palavra.upper()} temos :', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')