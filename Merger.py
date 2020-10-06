import os
import glob
import pandas as pd

#Selecciono el directorio donde tengo los archivos
os.chdir("C:/Users/gbalonga/Desktop/csv")

#Genero vector con el nombre de todos los archivos
all_filenames = [i for i in glob.glob('*.{}'.format("txt"))]
print (all_filenames)


#Genero el archivo "consolidado"

with open('Consolidado', 'w') as outfile:
    #fname, es la variable que pasa a tener el nombre del archivo en el cual se esta trabajando
    for fname in all_filenames:
        #abro fname y dentro de el opera
        with open(fname) as infile:
            #para cada linea dentro del archivo
            for line in infile:
                #agarro el nombre del archivo y le saco lo que molesta, para dejar unicamente la fecha
                Dia = fname[4:]
                temp = len(Dia)
                corte = Dia [:temp-4]
                #Escribo la linea en "consolidado" y paso a la linea siguiente
                outfile.write(corte  + " ," + line)

#Con el archivo consolidado, genero el archivo Datos.csv
#Agrego headers y cambio los = por ,
with open("consolidado", 'r') as f:
    with open("datos.csv", 'w') as t:
        t.write ("dia,hora,extra1, envio,extra2, Peso ,extra3,alto ,extra4,ancho ,extra5, largo,extra6, volumen,extra7,rampa,extra8, Modo ,extra9, Usuario" +'\n')
        for line in f:
            new_line = line.replace("=",",")
            t.write(new_line)


#Defino un Dataframe
df = pd.read_csv("datos.csv")
df.set_index(["dia","hora"])

#Borro todas las columnas extra (De la 1 a la 9)
for n in range (1,9):
    del df ["extra"+ str(n)]

#Paso el Df a el archivo CSV.
df.to_csv('datos.csv')
