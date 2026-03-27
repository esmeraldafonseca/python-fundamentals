def notas(*nota, sit=False):
    """
    Função para analisar notas e a situação de varios alunos
    :param nota: (aceita varios) as notas do aluno
    :param sit:a situação do aluno mediante as suas notas
    :return:
    """
    n1={}

    #total
    n1['Total']= len(nota)

    #maior
    n1['maior'] = max(nota)

    #menor
    n1['menor']= min(nota)

    #media
    n1['media']= sum(nota)/len(nota)

    #situação
    if sit == True:
        if n1['media'] >=7:
            n1['Situação'] = "BOA"
        elif n1['media'] <=7 and n1['media'] > 5:
            n1['Situação'] = "RAZOVEL"
        else:
            n1['Situação'] = "MA"

    return n1



#programa principal
resp = notas(10, 8, 10, sit=True)
print(resp)