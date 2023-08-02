LIMITE_SAQUES = 3
LIMITE = 500
numero_saques =0
saque = 0
deposito = 0.0
repeat = True
extrato = ""
saldo = 0
count_saques = 0

while True :
    print("Menu : ")
    print("1 : Depositar.")
    print("2 : Saquar.")
    print("3 : Ver Extrato.")
    print("4 : Exit")

    try:
        menu = int(input("Digite o numero da acao desejada: "))

    except:
        print("Input invalida")
        print("*************************")
        continue


    if(menu == 1):
      while (repeat):
        try:

          deposito = float(input("Digite o valor que voce deseja depositar: "))

        except:
          print("*************************")
          print("Valor do deposito invalido.")
          print("*************************")
          repeat = True
          continue

        if(deposito <= 0 ):
            repeat= True
            print("*************************")
            print("Valor do deposito invalido.")
            print("*************************")
            continue
        saldo += deposito
        extrato += f"/Deposito : R$ {deposito:.2f}/ "
        print("*************************")
        print(f"Deposito de R$ {deposito:.2f} feito com sucesso")
        print("*************************")
        repeat = False
    elif(menu == 2):
            while(repeat):
                try:

                    saque = float(input("Digite o valor que voce deseja saquar da conta: "))
                    repeat = False

                except:
                    print("*************************")
                    print("Valor de saque invalido.")
                    print("*************************")
                    repeat= True
                    continue
                if(saque <= saldo and count_saques < LIMITE_SAQUES and saque <= LIMITE and saque > 0   ):
                 print("*******************************************")
                 print(f"Saque de R$ {saque:.2f} retirado com sucesso")
                 print("*******************************************")
                 saldo -= saque
                 count_saques+=1
                 extrato+= f"Saque : R$ {saque:.2f}/ "
                 break


                elif(saque > saldo):
                 print("*******************************************")
                 print("Valor do saque maior do que o saldo disponivel.")
                 print("*******************************************")
                 repeat= True
                 continue



                elif(count_saques >=3):
                  print("*******************************************")
                  print("Voce nao pode fazer saques")
                  print("*******************************************")
                  break

                else:
                 print("*************************************************")
                 print("Voce nao pode retirar mais de 500 reais por saque")
                 print("*************************************************")
                 repeat = True
                 continue

    elif(menu==3):
           if(len(extrato) !=0):
            print("*************************************************")
            print(f"O seu extrato {extrato}.\nSeu saldo e de: R$ {saldo:.2f}" )
            print("*************************************************")
           else:
               print("Voce nao teve movimentacoes")

    elif(menu == 4):

         print("*************************************************")
         print("Ciao ciao")
         print("*************************************************")
         break

    else:

        print("*************************************************")
        print("O valor inputado nao e valido escolha de novo por favor")

        print("*************************************************")
    repeat=True







