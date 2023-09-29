'''n =str(input("entre com um numero"))
n = n.replace(',', '.').replace()
n = float(n)
print(n)
'''
lucro="1.000,02"  #tela.valapagar.get()
#if cnum1[cnum1.find('.') + 1] == '0':
if len(lucro[lucro.find(',')+1:]) == 2:
    print(lucro[lucro.find(',')+1:])
    
else:
     print(lucro[lucro.find(',')+1:])
     
print(lucro[lucro.find(',')+1])
print(lucro[lucro.find(',')+2])
#print(len(lucro[lucro.find(',')+3]))
#print(lucro[lucro.find(',')+4])
#if lucro.find('.') + 1 == '0':
#    print()

#lucro=float(lucro)
print(lucro) 
#texto_lucro = f'{lucro:_.2f}'
#print(texto_lucro)
#texto_lucro = lucro.replace('.',',').replace('_','.')
#print(texto_lucro)
while True:
    if lucro.find('.')==-1:
      break
    else:
      lucro = lucro.replace('.','')
      print(lucro)
lucro=lucro.replace(',','.')  
print(lucro)
#valor=valor.replace("_",",")
#print(valor)
valor=float(lucro)
print(f'O lucro foi de {valor-10}')


#Formato brasileiro do valor final