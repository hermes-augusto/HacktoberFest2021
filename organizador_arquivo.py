'''
    
Exemplo de como funciona neste arquivo apenas para explicar 
com os testes Para ver tudo, procure o arquivo
'''
import os, shutil, re, mimetypes, time, datetime


dirName = 'temp/'
dirNameTree = 'temp2/x/p/t/o'


#crie um dir único
if not os.path.exists(dirName):
    os.makedir(dirName)
    print("Directory " , dirName ,  " Created ")
else:
    print("Directory " , dirName ,  " already exists")


#crie uma árvore de dirs
if not os.path.exists(dirNameTree):
    os.makedirs(dirNameTree)
    print("Directory " , dirNameTree ,  " Created ")
else:    
    print("Directory " , dirNameTree ,  " already exists")


#Encontre todos os tipos de arquivos no nome do diretório anteriores e mostre todos os arquivos
[print(re.match("(.*?)/",mimetypes.guess_type(i)[0]).group(1)) for i in os.listdir() if '.' in i]

#Usando windowns dir para teste no meu computador

dir_test = 'D:\HermesAugusto\Documents\files'

#obter a data de criação e a data de modificação usando getmtime


#Formato da data do arquivoi yyyy-mm
time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime("new 3.txt"))))
#O primeiro tempo de obtenção do arquivo em segundos é retornar um flutuante
x = os.path.getctime("new 3.txt")
#converte a data para Fri Oct 29 20:30:15 2021
y = time.ctime(x)
#Convrerto to object time and transform to pattern yyyy-mm
t_obj = time.strftime("%Y-%m",time.strptime(y))

#walk in tree dirs using regx to get type each of file and printing this
for root, dirs, files in os.walk(dir_test):
    print("ROOT: ", root)
    print("dirs: ", dirs)
    print("files: ", files)
    
    [print(re.match("(.*?)/",mimetypes.guess_type(i)[0]).group(1)) for i in files ]
#fazendo a copia shutil
shutil.copy2('new 3.txt','D:\HermesAugusto\Documents\Projects\personal\study' )
#How make a move of file using shutil
shutil.move('new 3.txt','D:\HermesAugusto\Documents\Projects\personal\study')
