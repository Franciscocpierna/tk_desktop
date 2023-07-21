from time import sleep
def leiaInt1(msg):
  while True:
    try:
       n=int(input(msg))
    except (ValueError,TypeError):
       print('\n\033[31mErro: por favor, digite um número inteiro válido.\033[m')
    except (KeyboardInterrupt):
       print('\n\033[31mErro: por favor, digite um número inteiro válido.\033[m')
       return 0
    else:
       return n

def leiaFloat(msg):
  while True:
   try:
        n = str(input(msg))
        n = n.replace(',', '.')
        n = float(n)
   except (ValueError, TypeError):
          print('\033[0;31m erro: digite um numero real valido.\033[m')
          continue
   except (KeyboardInterrupt):
          print('\033[31mUsuário preferiu não digitar esse número:\033[m')
          return 0
   else:
          if (n // 1 == n):  # se a divisão por 1 igual n entao é inteiro se nao float
             n = int(n)
             return n

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n=str(input(msg))
        if n.isnumeric():
         valor = int(n)
         ok = True
        else:
          print ('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
             break
    return valor

def continua():
    while True:
        try:
            r=str(input('quer continuar:[S/N] ').upper()[0])
        except (KeyboardInterrupt):
            print('\n\033[31mErro: interrompeu execução\033[m')
            return 'N'
        except IndexError:
            print('\033[31mdigite opção valida S ou N: \033[m')
        else:
            if r not in "SN":
                 print('\033[31mdigite opção valida S ou N: \033[m')
            else:
                 return r

