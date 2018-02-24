#importes
import sys

#clase principal
class biblioteca():

    #def __init__(self):
    #    self.dato = "111"

    @staticmethod
    def imprimeTxt():
        archivo = open("catalogo.txt","r")
        print("CATALOGO DE LIBROS DE LA BIBLIOTECA DEL TEC")
        for linea in archivo.readlines():
            print(linea)

    @staticmethod
    def leeTxt(libro_solicitado, cantidad_solicitada):
        #print("loading....")
        archivo = open("catalogo.txt", "r+")
        contador = 0
        bandera = 0
        fila = 0
        libros = archivo.readlines()
        morosidad = 0
        for linea in libros:
            #si esta moroso el indicador estaria en 1
            if(morosidad == 0):
                #print("linea que estoy leyendo.."+linea)
                iterador = iter(linea)
                letra = next(iterador)
                contador = 0
                #print("letra.."+letra)
                libro = ""
                fila = fila + 1
                while (letra != ","):
                    libro += letra
                    letra = next(iterador)
                    contador = contador + 1
                
                if(libro == libro_solicitado):
                    print("FELICIDADES! su libro fue encontrado.."+libro)
                    letra = next(iterador)
                    contador = contador + 1
                    bandera = 1
                    if(letra >= cantidad_solicitada):
                        print("FELICIDADES! la cantidad solicitada esta disponible.."+letra)
                        #archivo.seek(contador)
                        columnas = libros[fila-1].split(',')
                        
                        cant_libros = int(columnas[1])
                        cant_soli = int(cantidad_solicitada)
                        cant_final = cant_libros - cant_soli
                        print("El libro solicitado: "+libro_solicitado+" queda con la cantidad disponible de: ")
                        print(cant_final)

                        #columnas[1] = cant_final
                        #archivo[fila-1] = ",".join(columnas)
                        #with open("catalogo.txt", "w") as arch:
                        #    arch.writelines(archivo)

                        print("Porfavor: entregar el libro antes de la fecha indicada o si no pasa a \n moroso y no podra hacer mas retiros de libros hasta que pague.")
                        return 1
                    else:
                        print("LO SENTIMOS, no hay la cantidad solicitada")
                        bandera = 0
                        return -1
                        
        if(bandera == 1):
            print("LO SENTIMOS, no encontramos su libro solicitado")
            return -1
        
        
#main
if __name__ == '__main__':
    
    sacarLibro = biblioteca()
    sacarLibro.imprimeTxt()

    libro = input("Inserte su libro a retirar: ")
    cantidad = input("Inserte la cantidad deseada: ")
    
    if(sacarLibro.leeTxt(libro, cantidad) == -1):
        libro = input("Inserte su libro a retirar: ")
        cantidad = input("Inserte la cantidad deseada: ")
        sacarLibro.leeTxt(libro, cantidad)

