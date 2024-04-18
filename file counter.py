import glob
import pandas as pd

base_path = r'T:\Recebimento Fiscal 2\Fretes\Faturas de Fretes\1 - FISCAL Conferência de Fretes\\'
prefix = '0'
folder = '1'
data = {
    'PASTA': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],
    'FISCAL': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    'TRANSPORTES': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    'CONFERIDOS': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    'OC_APROVADAS': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']    
    }
df = pd.DataFrame(data)
columns = ('PASTA','FISCAL','TRANSPORTES','CONFERIDOS','OC_APROVADAS')

############################################## FISCAL ##############################################

while (str(prefix) + str(folder)) != '010':     #considera do 01 ao 09
    dir_path = base_path + prefix + str(folder) #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    df.at[(folder-2),'FISCAL'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    df.at[(folder-2),'FISCAL'] = number_of_pdf_files

############################################## TRANSPORTES ##############################################

base_path = r'T:\Recebimento Fiscal 2\Fretes\Faturas de Fretes\2 - TRANSPORTES Conferência de Fretes\\'
folder = '1'

while (str(prefix) + str(folder)) != '010':     #considera do 01 ao 09
    dir_path = base_path + prefix + str(folder) #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    df.at[(folder-2),'TRANSPORTES'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    df.at[(folder-2),'TRANSPORTES'] = number_of_pdf_files

############################################## CONFERIDOS ##############################################

base_path = r'T:\Recebimento Fiscal 2\Fretes\Faturas de Fretes\3 - Fretes Conferidos\\'
folder = '1'

while (str(prefix) + str(folder)) != '010':     #considera do 01 ao 09
    dir_path = base_path + prefix + str(folder) #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    df.at[(folder-2),'CONFERIDOS'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    df.at[(folder-2),'CONFERIDOS'] = number_of_pdf_files

############################################## OC_APROVADAS ##############################################

base_path = r'T:\Recebimento Fiscal 2\Fretes\Faturas de Fretes\5 - Fretes OC Aprovadas\\'
folder = '1'

while (str(prefix) + str(folder)) != '010':     #considera do 01 ao 09
    dir_path = base_path + prefix + str(folder) #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    df.at[(folder-2),'OC_APROVADAS'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    df.at[(folder-2),'OC_APROVADAS'] = number_of_pdf_files

df.to_csv(r'C:\Users\eliances\Desktop\file_register\count.csv', index=False)