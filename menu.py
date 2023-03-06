from data import Slangs, session_create
from conexion import engine, base, session_create


base.metadata.create_all(engine)
session = session_create()

Slangs.insertar(session_create())


menu = True
while menu:
    print("*****MENU******"
           "\na. Agregar nueva palabra"
           "\nb. Editar palabra existente"
           "\nc. Eliminar palabra existente "
           "\nd. Ver listado de palabras "
           "\ne. Buscar significado de palabra "
           "\nf. Salir ")

    desicion = input("Que deseas hacer?: ")
    if desicion == 'a':
        palabra = input("Ingresa la palabra: ")
        significado = input("Ingresa el significado: ")
        
        nuevo = Slangs(palabra, significado)
        
        session.add(nuevo)
        session.commit()

    elif desicion == 'b':
        value = input("Ingresa el ID de la palabra que deseas editar: ")
        editado = session.query(Slangs).filter(Slangs.id == value).first()
        
        editado.palabra = input("Ingresa la nueva palabra: ")
        editado.significado = input("Ingresa el nuevo significado: ")
        
        session.commit()
        
    elif desicion == 'c':
        value = input("Ingresa el ID de la palabra que deseas eliminar: ")
        eliminado = session.query(Slangs).filter(Slangs.id == value).first()
        
        if eliminado:
            session.delete(eliminado)
            print(f'La palabra {eliminado.palabra} ha sido eliminada')
            session.commit()
        else:
            print("No existe esa palabra")
        
    elif desicion == 'd':
        valores = session.query(Slangs).all()
        for columna in valores:
            print(f"id: {columna.id}. {columna.palabra}: {columna.significado}")

    elif desicion == 'e':
        value = input("Ingresa la palabra que deseas buscar: ")
        busqueda = session.query(Slangs).filter(Slangs.palabra == value).first()
        
        if busqueda:
            print(f"{busqueda.palabra}: {busqueda.significado}")
        else:
            print("No existe esa palabra")
            
    elif desicion == 'f':
        print("Gracias por usar el programa")
        break
    
    else: 
        print("**ERROR, informacion no disponible**")
        