def leiaMoney(n):
   valido = False

   while not valido:
       entra = str(input(n)) .replace(',','.')
       if entra.strip() == '' or not entra.replace('.', '', 1).isdigit():
           print(f'ERRO. {entra} é um preço invalido')
       else:
           valido =  True
           return float(entra)