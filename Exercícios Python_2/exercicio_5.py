def linha(tam=74):
    return '=' * tam

def linha_2(bungas):
    print(linha())
 

def centralizar(txt):
    print(linha())
    print(txt.center(70))
    print(linha())

from time import sleep
centralizar('Seja bem vindo !')
print()
listaum = []
for v in range(0, 5):




    listaum.append(int(input('Insira um numero : ')))
print()

centralizar('>>>>>    Aguarde ate o resultado da media entre os numeros inseridos') 
sleep(3)

centralizar('A média dos valores inseridos foi: {} '.format(sum(listaum) / len(listaum) ))
sleep(2)

centralizar('FIM....')