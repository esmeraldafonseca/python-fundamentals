from datetime import datetime

nome = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
data = datetime.now().year
idade = data - nasc

carteira = int(input("Carteira de trabalho(0 se não tiver): "))
dados = {'nome': nome,
             'idade': idade,
             }

if carteira ==0:
    print(f'{dados["nome"]} tem {dados["idade"]} de idade, NUNCA trabalhou')
else:
    dados['ctf'] = carteira
    AnoContrat = int(input("Ano de contratação: "))
    sal = float(input("Salario:"))
    anotrab = datetime.now().year - AnoContrat
    if anotrab >= 63:
        print(f'Está em idade de reforma')
    else:
        refor = 63 - anotrab
        dados['reforma']= refor
print("-="*30)
for v,k in dados.items():
    print(f'    -{v} tem {k}')





