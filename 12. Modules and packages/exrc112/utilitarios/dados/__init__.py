def leiaMoney(n):
   valido = False

   while not valido:
       entra = str(input(n)) .replace(',','.')
       if entra.isalnum() or entra == '':
           print(f'ERRO. {entra} é um preço invalido')
       else:
           valido =  True
           return float(entra)