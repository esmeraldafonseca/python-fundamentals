import json

def guardar_alunos(alunos):
    with open("alunos.json", "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4)

def carregar_alunos():
    with open("alunos.json", "r", encoding="utf-8") as f:
        return json.load(f)

def media_turma(alunos):
    notas = 0
    for itens in alunos:
        notas += itens["Notas"]
    media = notas/len(alunos)
    return media


def aprovados_alunos(alunos):
    aprovados = []
    for itens in alunos:
        if itens["Notas"] >= 10:
            aprovados.append(itens)
    return aprovados

