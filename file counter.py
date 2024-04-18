import glob
import pandas as pd

data_frame0 = pd.DataFrame({
    'Qtda': ['0']
})

data_frame1 = pd.DataFrame({
    'Vecto': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],
    'Qtda': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
})
data_frame2 = pd.DataFrame({
    'Vecto': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],
    'Qtda': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
})
data_frame3 = pd.DataFrame({
    'Vecto': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],
    'Qtda': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
})
data_frame4 = pd.DataFrame({
    'Vecto': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],
    'Qtda': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
})
data_frame5 = pd.DataFrame({
    'Vecto': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],
    'Qtda': ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
})
#df = pd.DataFrame(data)
#columns = ('PASTA','FISCAL','TRANSPORTES','CONFERIDOS','OC_APROVADAS')

prefix = '0'
folder = '1'

base_path = r'T:\Recebimento Fiscal 2\Fretes\Faturas de Fretes\0 - E-mail de Faturas'


dir_path = base_path                        #define o nome do diretorio a ser lido
#count = 0                                  #define uma partida zero
pdf_files = glob.glob(f'{dir_path}/*.eml')  #Padrão de apenas PDFs
number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
print(f"{str(folder)} - {number_of_pdf_files}.")
data_frame0.at[0,'Qtda'] = number_of_pdf_files

############################################## FISCAL ##############################################
base_path = r'T:\Recebimento Fiscal 2\Fretes\Faturas de Fretes\1 - FISCAL Conferência de Fretes\\'


while (str(prefix) + str(folder)) != '010':     #considera do 01 ao 09
    dir_path = base_path + prefix + str(folder) #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    data_frame1.at[(folder-2),'Qtda'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    data_frame1.at[(folder-2),'Qtda'] = number_of_pdf_files

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
    data_frame2.at[(folder-2),'Qtda'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    data_frame2.at[(folder-2),'Qtda'] = number_of_pdf_files

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
    data_frame3.at[(folder-2),'Qtda'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    data_frame3.at[(folder-2),'Qtda'] = number_of_pdf_files

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
    data_frame4.at[(folder-2),'Qtda'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    data_frame4.at[(folder-2),'Qtda'] = number_of_pdf_files

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
    data_frame5.at[(folder-2),'Qtda'] = number_of_pdf_files

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    #count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta
    data_frame5.at[(folder-2),'Qtda'] = number_of_pdf_files



with pd.ExcelWriter(r'C:\Users\eliances\Desktop\file_register\Controle_de_Faturas.xlsx', engine='openpyxl') as writer:
    data_frame0.to_excel(writer, sheet_name='0 - E-mail de Faturas', index=False)
    data_frame1.to_excel(writer, sheet_name='1 - FISCAL Conferência de Frete', index=False)
    data_frame2.to_excel(writer, sheet_name='2 - TRANSPORTES Conferência de ', index=False)
    data_frame3.to_excel(writer, sheet_name='3 - Fretes Conferidos', index=False)
    data_frame4.to_excel(writer, sheet_name='4 - Fretes Requisição de Compra', index=False)
    data_frame5.to_excel(writer, sheet_name='5 - Fretes OC Aprovadas', index=False)
#df.to_csv(r'C:\Users\eliances\Desktop\file_register\count.xlsx', index=False)