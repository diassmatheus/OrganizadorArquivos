import os

lista_tudo = os.listdir()

lista_diretorios =[]

for i in lista_tudo:
    if os.path.isdir(i) is True:
        lista_diretorios.append(i)

for i in lista_diretorios:
    diretorio = os.getcwd() + '\\' + i
    arquivos_no_diretorio = os.listdir(diretorio)
    for j in arquivos_no_diretorio:
        os.rename(diretorio+'/'+j, j)
    os.rmdir(diretorio)