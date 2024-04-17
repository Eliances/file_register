import glob

base_path = r'T:\Recebimento Fiscal 2\Fretes\Faturas de Fretes\1 - FISCAL Conferência de Fretes\\'
prefix = '0'
folder = '1'
while (str(prefix) + str(folder)) != '010':     #considera do 01 ao 09
    dir_path = base_path + prefix + str(folder) #define o nome do diretorio a ser lido
    count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta

while str(folder) != '32':                      #Considera do 10 ao 31
    dir_path = base_path + str(folder)          #define o nome do diretorio a ser lido
    count = 0                                   #define uma partida zero
    pdf_files = glob.glob(f'{dir_path}/*.pdf')  #Padrão de apenas PDFs
    number_of_pdf_files = len(pdf_files)        #Lê a quantidade de itens na pasta
    print(f"{str(folder)} - {number_of_pdf_files}.")
    folder = int(folder) + 1                    #Vai para a próxima pasta