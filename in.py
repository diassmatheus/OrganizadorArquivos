import os

lista_tudo = os.listdir()

lista_arquivos =[]

for i in lista_tudo:
    if os.path.isfile(i) is True:
        lista_arquivos.append(i)

lista_arquivos_sem_py = []

for i in lista_arquivos:
    if i.split('.')[-1] != 'py':
        lista_arquivos_sem_py.append(i)

lista_extencoes = []

for i in lista_arquivos_sem_py:
    lista_extencoes.append(i.split('.')[-1])

for i in set(lista_extencoes):
    if i not in os.listdir():
        os.mkdir(i)

for i in lista_arquivos_sem_py:
    extencao = i.split('.')[-1]
    os.rename(i, extencao+'/'+i)