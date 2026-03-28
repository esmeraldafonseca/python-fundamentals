from utilitarios import moeda
from utilitarios import dados


preço = dados.leiaMoney("Digite o preço: ")
moeda.resumo(preço)