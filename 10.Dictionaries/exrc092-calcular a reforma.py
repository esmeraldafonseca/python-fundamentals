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
    print(f'{dados["nome"]} tem {dados["idade"]} anos de idade, NUNCA trabalhou')
else:
    dados['ctf'] = carteira
    AnoContrat = int(input("Ano de contratação: "))
    sal = float(input("Salario:"))
    dados['contratação'] = AnoContrat
    dados['salario'] = sal
    # reforma com 35 anos de contribuição
    dados['reforma'] = (AnoContrat + 35) - nasc
print("-="*30)
for v,k in dados.items():
    print(f'    -{v} tem {k}')





