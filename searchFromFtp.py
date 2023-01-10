"""
Este pequeño script extrae todos los arhivos logs en un directorio y luego busca errores 
en el envio de transacciones a bopos suite, los obtiene y genera txts por cada uno

@author Daniel Mendoza
"""

import ftplib
from datetime import datetime, timedelta
import os

## Creamos el directorio donde quedaran los logs que encontremos
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'archivos_ftp')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

## Creamos el directorio donde quedaran las transacciones que encontramos
transaction_directory = os.path.join(current_directory, r'transacciones')
if not os.path.exists(transaction_directory):
   os.makedirs(transaction_directory)

## Obtenemos los ultimos 3 días
d1 = datetime.today() - timedelta(days=1)
d2 = datetime.today() - timedelta(days=2)
d3 = datetime.today() - timedelta(days=3)

## Formateamos los ultimos 3 dias
logFile1 =  "bsagent.log." + d1.strftime('%Y-%m-%d')
logFile2 =  "bsagent.log." + d2.strftime('%Y-%m-%d')
logFile3 =  "bsagent.log." + d3.strftime('%Y-%m-%d')

ftp = ftplib.FTP("10.17.12.39")
ftp.login("ftpuser", "4690tcpip")

ftp.cwd('f:\\bsagent')

files = ftp.nlst()

filesToSearch = [logFile1, logFile2, logFile3]

for fileToSearch in filesToSearch:
    if (fileToSearch in  files):
        print(f"--- Encontre el archivo con nombre {fileToSearch}")
        print(f"--- Descargando {fileToSearch}")
        ftp.retrbinary("RETR " + fileToSearch, open(f"{final_directory}\\"+fileToSearch, 'wb').write)

ftp.quit()

## Obtenemos el directorio y listamos solo los arhivos
files = os.listdir(final_directory)
files = [f for f in files if os.path.isfile(final_directory+'/'+f)] 

## Iteramos sobre los archivos
for file in files:
    print(f"--- Validando archivo: {file}")
    ## Abrimos los archivos, el unico encode que me funciono fue el cp437
    openFile = open(f"{final_directory}\\{file}","r", encoding="cp437")
    fileLines = openFile.readlines()
    lineNumber = 0

## Iteramos sobre las lineas de cada archivo, buscando el error de persistencia
error_count = 0
for line in fileLines:
    if line.find("BSConnector API has been encountered an error sending request.") != -1:
        print(f"--- Encontre un error en la linea {lineNumber + 1}")
        error_count + error_count + 1
        
        ## Buscamos el final del error para añadirlo al archivo txt
        errorCount = 0
        for j in range(lineNumber+1, lineNumber+1000, 1):
            if fileLines[j][0].isdigit() == False:
                errorCount= errorCount + 1
            else:
                break

        ## Buscamos el inicio del poslog 
        poslog = ""
        transacionId = "0"
        for i in range(lineNumber+errorCount, 0, -1):
            ## Obtenemos el transactionId
            if fileLines[i].find("Sending Transaction with ID:") != -1:
                print(fileLines[i][-32:])
                transacionId = fileLines[i][-32:].replace("\n","")

            if fileLines[i].find("Extensions Succesfull Executed !!") != -1:
                break
            
            poslog =  fileLines[i] + poslog

        ## Si no encontramos el transactionId, le colocamos el numero de linea
        if transacionId == "0": 
            transacionId = lineNumber

        ## Creamos archivo txt para guardar transaccion
        txtFile = f= open(f"{final_directory}\\{transacionId}.txt","w+",encoding="cp437")
        txtFile.write(poslog)
        txtFile.close()
    lineNumber = lineNumber + 1 
print(f"--- Proceso terminado, se encontraron {error_count} transacciones con error")
