import os
from colorama import Fore
from time import sleep
print(Fore.LIGHTYELLOW_EX+'''
                                                                                                                        
    EEEEEEEEEEEEEEEEEEEEEE             AAA                  GGGGGGGGGGGGG   LLLLLLLLLLL               EEEEEEEEEEEEEEEEEEEEEE
    E::::::::::::::::::::E            A:::A              GGG::::::::::::G   L:::::::::L               E::::::::::::::::::::E
    E::::::::::::::::::::E           A:::::A           GG:::::::::::::::G   L:::::::::L               E::::::::::::::::::::E
    EE::::::EEEEEEEEE::::E          A:::::::A         G:::::GGGGGGGG::::G   LL:::::::LL               EE::::::EEEEEEEEE::::E
    E:::::E       EEEEEE           A:::::::::A       G:::::G       GGGGGG   L:::::L                   E:::::E       EEEEEE
    E:::::E                       A:::::A:::::A     G:::::G                 L:::::L                   E:::::E             
    E::::::EEEEEEEEEE            A:::::A A:::::A    G:::::G                 L:::::L                   E::::::EEEEEEEEEE   
    E:::::::::::::::E           A:::::A   A:::::A   G:::::G    GGGGGGGGGG   L:::::L                   E:::::::::::::::E   
    E:::::::::::::::E          A:::::A     A:::::A  G:::::G    G::::::::G   L:::::L                   E:::::::::::::::E   
    E::::::EEEEEEEEEE         A:::::AAAAAAAAA:::::A G:::::G    GGGGG::::G   L:::::L                   E::::::EEEEEEEEEE   
    E:::::E                  A:::::::::::::::::::::AG:::::G        G::::G   L:::::L                   E:::::E             
    E:::::E       EEEEEE    A:::::AAAAAAAAAAAAA:::::AG:::::G       G::::G   L:::::L         LLLLLL    E:::::E       EEEEEE
    EE::::::EEEEEEEE:::::E  A:::::A             A:::::AG:::::GGGGGGGG::::G  LL:::::::LLLLLLLLL:::::L  EE::::::EEEEEEEE:::::E
    E::::::::::::::::::::E  A:::::A               A:::::AGG:::::::::::::::G L::::::::::::::::::::::L  E::::::::::::::::::::E
    E::::::::::::::::::::E  A:::::A                 A:::::A GGG::::::GGG:::GL::::::::::::::::::::::L  E::::::::::::::::::::E
    EEEEEEEEEEEEEEEEEEEEEE  AAAAAAA                   AAAAAAA   GGGGGG   GGGGLLLLLLLLLLLLLLLLLLLLLLLL EEEEEEEEEEEEEEEEEEEEEE
                                                                                                                     
                                                                                    
''')
print(Fore.RED+"EAGLE 🦅 ")
print(Fore.LIGHTGREEN_EX+"Iniciando...")
x=input(f"Digite o nome de usuário do seu computador:") #Caso não saiba vá em C:\Users\Seu_nome_de_usuario_aqui
if os.path.exists(f'C:\\Users\\{x}') is True:
    desktop = os.listdir(f'C:\\Users\\{x}\\Desktop')
    print(Fore.RED + "ESCANEANDO DESKTOP...")
    sleep(2)
    print(Fore.BLUE + "Lista de Arquivos/Diretórios Encontrados:", desktop)
    so = os.name
    sleep(2)
    if so == 'nt':
        print(Fore.GREEN + "Sistema Operacional: Windows")
        criar = input(Fore.BLUE + "Deseja criar um arquivo:[s/n]")
        if criar == 's':
            try:
                print("Digite [1] para criar na Área de Trabalho")
                print("Digite [2] para criar em Downloads")
                print("Digite [3] para criar em Documents")
                op = int(input("Digite o número:"))
                if op == 1:
                    print(Fore.BLUE + "Criando Arquivo na Área de Trabalho")
                    sleep(2)
                    if criar == 's':
                        arquivo = input('Nome do Arquivo:')
                        print('Apenas arquivos de texto serão criados')
                        sleep(2)
                        print(Fore.BLUE + 'Criando Arquivo TXT')
                        with open(f'C:\\Users\\{x}\\Desktop\\{arquivo}.txt', 'w') as file:
                            file.write('BY:KAMIKAZE')
                        if os.path.exists(f'C:\\Users\\{x}\\Desktop\\{arquivo}.txt') is True:
                            print(Fore.YELLOW + "Arquivo Criado Com Sucesso =)")
                            print(Fore.RED + "Reinicie o programa caso queira refazer o processo...")
                            print(Fore.GREEN + "BY:KAMIKAZE")
                        else:
                            print(Fore.RED + "Arquivo Não Foi Criado =(")
                            print(Fore.RED + "Reinicie o programa para tentar novamente...")
                            print(Fore.GREEN + "BY:KAMIKAZE")
                    elif criar == 'n':
                        print(Fore.RED + "Nenhum Arquivo Criado =( ")
                        print("Programa Finalizado")
                        print(Fore.GREEN + "BY:KAMIKAZE")
                    else:
                        print(Fore.RED + 'Opção Inválida =(')
                        print(Fore.RED + 'Digite s [sim] ou n [não]!')
                        print(Fore.BLUE + 'Reinicie o programa...')
                elif op == 2:
                    print(Fore.BLUE + "Criando Arquivo em Downloads...")
                    sleep(2)
                    if criar == 's':
                        arquivo = input('Nome do Arquivo:')
                        print('Apenas arquivos de texto serão criados')
                        sleep(2)
                        print(Fore.BLUE + 'Criando Arquivo TXT')
                        with open(f'C:\\Users\\{x}\\Downloads\\{arquivo}.txt', 'w') as file:
                            file.write('BY:KAMIKAZE')
                        if os.path.exists(f'C:\\Users\\{x}\\Downloads\\{arquivo}.txt') is True:
                            print(Fore.YELLOW + "Arquivo Criado Com Sucesso =)")
                            print(Fore.RED + "Reinicie o programa caso queira refazer o processo...")
                            print(Fore.GREEN + "BY:KAMIKAZE")
                        else:
                            print(Fore.RED + "Arquivo Não Foi Criado")
                            print(Fore.RED + "Reinicie o programa para tentar novamente...")
                    elif criar == 'n':
                        print(Fore.RED + "Nenhum Arquivo Criado =( ")
                        print("Programa Finalizado")
                        print(Fore.GREEN + "BY:KAMIKAZE")
                    else:
                        print(Fore.RED + 'Opção Inválida =( ')
                        print(Fore.RED + 'Digite s [sim] ou n [não]!')
                        print(Fore.BLUE + 'Reinicie o programa...')
                        print(Fore.GREEN + "BY:KAMIKAZE")
                elif op == 3:
                    print(Fore.BLUE + "Criando Arquivo em Documents...")
                    sleep(2)
                    if criar == 's':
                        arquivo = input('Nome do Arquivo:')
                        print('Apenas arquivos de texto serão criados')
                        sleep(2)
                        print(Fore.BLUE + 'Criando Arquivo TXT')
                        with open(f'C:\\Users\\{x}\\Documents\\{arquivo}.txt', 'w') as file:
                            file.write('BY:KAMIKAZE')
                        if os.path.exists(f'C:\\Users\\{x}\\Documents\\{arquivo}.txt') is True:
                            print(Fore.YELLOW + "Arquivo Criado Com Sucesso =)")
                            print(Fore.RED + "Reinicie o programa caso queira refazer o processo...")
                            print(Fore.GREEN + "BY:KAMIKAZE")
                        else:
                            print(Fore.RED + "Arquivo Não Foi Criado")
                            print(Fore.RED + "Reinicie o programa para tentar novamente...")
                            print(Fore.GREEN + "BY:KAMIKAZE")
                    elif criar == 'n':
                        print(Fore.RED + "Nenhum Arquivo Criado =( ")
                        print("Programa Finalizado")
                        print(Fore.GREEN + "BY:KAMIKAZE")
                    else:
                        print(Fore.RED + 'Opção Inválida =(')
                        print(Fore.RED + 'Digite s [sim] ou n [não]!')
                        print(Fore.BLUE + 'Reinicie o programa...')
                        print(Fore.GREEN + "BY:KAMIKAZE")
                else:
                    print(Fore.RED + "Opção Inválida =(")
                    print(Fore.RED + "Digite 1,2 ou 3")
                    print(Fore.GREEN + "BY:KAMIKAZE")

            except:
                print(Fore.RED + "Digite um Número Inteiro [1,2 ou 3]")
                print(Fore.RED + "Reinicie o programa!")
                print(Fore.GREEN + "BY:KAMIKAZE")
        elif criar == 'n':
            print(Fore.BLUE + "Fim do Programa =)")
            print(Fore.GREEN + "BY:KAMIKAZE")
        else:
            print(Fore.RED + "Opção Inválida =( ")
            print(Fore.RED + "Digite s para sim e n para não")
            print(Fore.RED + "Reinicie o Programa")
            print(Fore.GREEN + "BY:KAMIKAZE")
    elif so == 'posix':
        print(Fore.RED + "Sistema Operacional: Linux")
        print(Fore.LIGHTBLUE_EX + "Diretório Atual:", os.getcwd())
        sleep(2)
        print(Fore.RED + "Versão Para Linux Em Construção...")
        print(Fore.GREEN + "BY:KAMIKAZE")
    else:
        print(Fore.BLUE + "Sistema Operacional: Não Identificado")
        sleep(2)
        print(Fore.RED + "Versão para outros Sistemas Operacionais em Construção...")
        print(Fore.GREEN + "BY:KAMIKAZE")
else:
    print(Fore.RED+"Usuário Não Encontrado =(")
    print(Fore.RED+"Reinicie o programa...")
    print(Fore.GREEN+"BY:KAMIKAZE")


