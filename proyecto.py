from pathlib import Path

current_path = Path.cwd()
file_path = Path(current_path)

def menu():
    print ('Menú')
    print ('1) Listar documentos')
    print ('2) Leer documento')
    print ('3) Eliminar documento') 
    print ('4) Terminar de consultar') 

def listado():
    for archivo in file_path.iterdir():
    
        if archivo.is_file() and  archivo.suffix == '.txt':
            print(archivo.name)

def lectura():
    documento = input('Nombre del archivo: ')
    ruta = current_path / documento

    nombre = open(ruta, 'r')
    archivo = nombre.read()
    nombre.close()
    print(archivo)

def eliminar():
    nombre = input('Nombre del archivo: ')
    ruta = current_path / nombre
    ruta.unlink()


menu()
opcion = int(input('¿Qué opción quiere?: '))

while opcion:
    if opcion == 1:
        listado()
    elif opcion == 2:
        lectura()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        print ('Consulta Terminada')
        break
    menu()
    opcion = int(input ('¿Qué opción quiere?: '))