sal = float(input('Digite o salario do funcionario:'))

if sal > 1250.00 :
    aumento = sal * 0.10
    print('Receberás um aumento de 10% e o seu salario sera de: {}'.format(sal + aumento))

if sal <= 1000.00 :
    aumento = sal * 0.15
    print('Receberás um aumento de 15% e o seu slaraio será de : {}'.format(sal + aumento))

