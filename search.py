"""
Este pequeño script revisa todos los archivos en un directorio en busca de errores 
en el envio de transacciones a bopos suite, los obtiene y genera txts por cada uno

@author Daniel Mendoza
"""
import os

Direc = input(r"Ingrese la ruta de la carpeta donde estan los logs: ")
#Direc = 'D:\logsqa\BSAGENT\missingtrx'
print(f"Archivos en el directorio: {Direc}")

## Creamos el directorio donde quedaran las transacciones que encontramos
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'transacciones')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

## Obtenemos el directorio y listamos solo los arhivos
files = os.listdir(Direc)
files = [f for f in files if os.path.isfile(Direc+'/'+f)] 

## Iteramos sobre los archivos
error_count = 0
for file in files:
    print(f"Validando archivo: {file}")
    ## Abrimos los archivos, el unico encode que me funciono fue el cp437
    openFile = open(f"{Direc}\\{file}","r", encoding="cp437")
    fileLines = openFile.readlines()
    lineNumber = 0

    ## Iteramos sobre las lineas de cada archivo, buscando el error de persistencia
    
    for line in fileLines:
        if line.find("BSConnector API has been encountered an error sending request.") != -1:
            print(f"Encontre un error en la linea {lineNumber + 1}")
            error_count = error_count + 1

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

    
