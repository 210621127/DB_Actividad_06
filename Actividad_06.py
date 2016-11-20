"""
Nombre: Rodriguez Bocanegra, Juan Daniel
Materia: Seminario de Solucion de Problemas de Bases de datos
Profesor: Michel Davalos Boites

Actividad 05 (INSERT INTO)
Implementar todos los "INSERT" que requiere el software: correo nuevo,
crear contacto, etc. Subir reporte con capturas de pantalla de la ejecución
del programa, el .sql y el .py (o repositorio).
"""
import sqlite3
import os
import time
import getpass

class Usuario():
    def __init__(self, data):
        self.correo = data
        self.contra = data
        self.apellidoPatU = data
        self.apellidoMatU = data
        self.nombresU = data
    def __str__ (self):
        return "\n\tCorreo: "+str(self.correo)+"\n\tContraseña: "+str(self.contra)\
            +"\n\tNombre: "+str(self.apellidoPatU)+" "+str(self.apellidoMatU)+","\
            +str(self.nombresU)+"\n\tContactos registrados: "+str(self.contRegistrados)

class Contacto():
    def __init__(self,data):
        self.contacto_id = data
        self.email = data
        self.registra = data
        self.apellidoPatC = data
        self.apellidoMatC = data
        self.nombresC = data

class Correo():
    def __init__(self, data):
        self.correo_id = data
        self.fecha = data
        self.hora = data
        self.de = data
        self.para = data
        self.para_id = data
        self.texto = data
        self.asunto = data
        self.adjunto = data
        self.eliminado = data

class MenuCorreoEnviado():
    def __init__(self):
        pass

class MenuContatos():

    def __init__(self):
        pass
    def agregar(self, user, db):
        u = user
        cursor = db.cursor()
        c = Contacto(None)
        print("\n\t* * * Agregar contacto * * *\n")
        print("\n\tPresione solo <ENTER> para regresar...")

        c.email = input("\n\tIngrese el correo del contacto: ")
        while len(c.email) < 1:
            return
        while len(c.email) < 2: #modificar para que reconozca minimo 8 caracteres
            print("\n\t(!) Ingrese un correo valido!")
            c.email = input ("\tCorreo: ")

        c.registra = u.correo
        c.apellidoPatC = input("\tApellido paterno: ")
        while len(c.apellidoPatC) < 1 :
            c.apellidoPatC = input("\t(!) Ingrese un apellido valido: ")
        c.apellidoMatC = input("\tApellido materno: ")

        c.nombresC = input("\tNombres(s): ")
        while len(c.nombresC) < 1:
            c.nombresC = input("\t(!) Ingrese un nombre valido: ")

        cursor.execute("INSERT INTO CONTACTO(contacto_id,email,registra,\
        apellidoPatC,apellidoMatC,nombresC) VALUES (?,?,?,?,?,?)", \
        (c.contacto_id,c.email,c.registra,c.apellidoPatC,c.apellidoMatC,c.nombresC))

        db.commit()
        input("\n\tContacto registrado satisfactoriamente...")


    def menu(self,user,db):

        opc = -1
        while True:
            os.system("clear")
            print("\n\t* * * CONTACTOS * * * \n")
            #print("\n\t1) Mostrar contactos ") # Muestra contactos - con id-
            print("\t2) Agregar nuevo contacto") #Agrega un nuevo contacto -correo-
            #print("\t3) Eliminar contacto") # Elimina de la base de datos (submenu)
            #print("\t4) Modificar contacto") # Modifica un contacto (submenu)
            print("\t0) Salir")
            opc = input ("\n\tIngrese una opcion: ")
            if opc.isdigit() == True:
                opc = int(opc)
                if opc == 1:
                    pass
                elif opc == 2:
                    os.system("clear")
                    self.agregar(user,db)
                elif opc == 3:
                    pass
                elif opc == 4:
                    pass
                elif opc == 0:
                    db.commit()
                    break


class MenuCorreoNuevo():
    def __init (self):
        pass
    def menu(user,db):
        menuC = MenuContatos()
        u = user
        cursor = db.cursor()
        c = Correo(None)

        while True:
            os.system("clear")
            print("\n\t* * * Correo Nuevo* * *\n")

            ahora = time.strftime("%c")
            c.fecha = time.strftime("%x")

            c.hora = time.strftime("%X")
            print("\tFecha: ", c.fecha)
            print("\tHora:  ",c.hora)

            c.de = u.correo
            print("\tDe:    ",c.de)

            c.para = input("\tPara:  ")
            while len(c.para) < 1:
                c.para = input("\tIngrese un correo valido: ")
            rows = cursor.execute("SELECT * FROM CONTACTO WHERE email = ? AND \
                registra = ?", (c.para, u.correo))
            for row in rows:
                c.para_id = row[0]

            if  c.para_id != None:
                break
            else:
                print("\n\t(!) El contacto que escribio no esta registrado...")
                input("\tPresione una tecla para continuar...")
                menuC.agregar(user,db)


        linea = ''
        print("\n\tPresione solo <ENTER> para continuar o escriba el texto...")
        c.texto = input("\tTexto:\n\t")
        while True and len(c.texto) > 0:
            linea = input("\t")
            if len(linea) < 1:
                break
            c.texto += '\n'+linea
        if len(c.texto ) == 0:
            c.texto = None

        c.asunto = input("\tAsunto: ")
        if len(c.asunto) == 0:
            c.asunto = None

        c.adjunto = input("\tAdjunto: ")
        if len(c.adjunto) == 0:
            c.adjunto = None

        c.eliminado = False

        ahora = time.strftime("%c")
        c.fecha = time.strftime("%x")
        c.hora = time.strftime("%X")

        cursor.execute("INSERT INTO CORREO (correo_id,fecha,hora,de,para,\
        para_id,texto,asunto,adjunto,eliminado) VALUES (?,?,?,?,?,?,?,?,?,?)",\
        (c.correo_id,c.fecha,c.hora,c.de,c.para,c.para_id,c.texto,c.asunto,\
        c.adjunto,c.eliminado))

        input("\n\tCorreo guardado exitosamente!")
        db.commit()

class MainMenu():

    def __init__(self):
        pass
    def menuGeneral(self,user,db):
        mNuevo = MenuCorreoNuevo()
        mEnviado = MenuCorreoEnviado()
        mContactos = MenuContatos()
        u = user
        db = db
        op = -1
        while True:
            os.system("clear")
            print("\n\tMENU GENERAL CORREOS\n\n\t1) Correo enviado\n\t2) Contactos \
                \n\t3) Correo nuevo\n\t0) Salir")
            op = input("\n\tOpcion:")
            while op.isdigit() == False:
                op = input("\n\t(!) Ingrese una opcion del menu: ")

            op = int(op)

            if op == 1:
                os.system("clear")
                print ("(!) Modulo no implementado...")
            elif op == 2:
                os.system("clear")
                mContactos.menu(user,db)
            elif op == 3:
                os.system("clear")
                MenuCorreoNuevo.menu(user,db)
            elif op == 0:
                db.commit()
                break
            else:
                input("\n\t(!) Ingrese una opcion del menu...")

class Login_Registro():
    db = sqlite3.connect("db_correos.db")
    #c = db.cursor(), c.execute("PRAGMA foreign_keys = ON")

    mg = MainMenu()
    user = Usuario(None)

    def __init__(self):
        pass

    def login(u,db):
        while True:
            u = u
            db = db
            c = db.cursor()

            os.system("clear")
            print("\n\t* * * LOGIN * * *\n\t(Presione <ENTER> para regresar)")
            usuario = input("\n\tUsuario: ")
            if usuario == '':
                break
            contra = getpass.getpass ("\n\tContraseña: ")

            rows = c.execute ('SELECT * FROM USUARIO WHERE correo = ? AND \
                contra = ?',(usuario, contra))
            for row in rows:
                u.correo = row[0]
                u.contra = row[1]
                u.apellidoPatU = row[2]
                u.apellidoMatU = row[3]
                u.nombresU = row[4]

            if u.correo != None:
                input("\n\tLogin correcto!")

                return True
            else:
                input("\n\t(!) Usuario o contraseña incorrectos!!")

    def registrarse(u,d):
        user = u
        db = d
        c = db.cursor()
        while True:
            print("\n\t* * * Registro * * * \n\t(Presione <ENTER> para regresar)")
            user.correo = input ("\n\tCorreo: ")
            if user.correo == '':
                break

            while True:
                pass1 = getpass.getpass("\tContrañena: ")
                pass2 = getpass.getpass("\tIngrese de nuevo la contraseña: ")
                if pass1 != pass2 :
                    print("\n\t(!) Las contraseñas no coinciden!")
                if len(pass1) < 1:
                    print("\n\t(!) Ingrese una contraseña valida")
                else:
                    if pass1 == pass2:
                        user.contra = pass1
                        break

            user.apellidoPatU = input("\tApellido paterno: ")
            while user.apellidoPatU.isalnum() == False:
                print("\n\t(!) Apellido invalido!")
                user.apellidoPatU = input ("\tIngrese su apellido paterno de nuevo: ")

            user.apellidoMatU = input("\tApellido Materno: ")

            user.nombresU = input("\tNombre(s): ")
            while len(user.nombresU) < 1:
                print("(!) Nombre invalido!")
                user.nombresU = input("\tIngrese su nombre de nuevo: ")
            c.execute("INSERT INTO USUARIO (correo,contra,apellidoPatU,\
                apellidoMatU,nombresU) VALUES (?,?,?,?,?)",\
                (user.correo, user.contra,user.apellidoPatU,user.apellidoMatU,\
                user.nombresU))
            db.commit()
            break

    while True:
        os.system("clear")
        print("\n\t* * * INICIO DE SESION/REGISTRO * * * \n\n\t1) Iniciar sesion \
            \n\t2) Registrarse \n\t0) Salir")
        op = input("\n\tElige una opcion: ")

        while op.isdigit() == False:
            op = input ("(!) Ingrese una de las opciones: ")

        op = int (op)

        if op == 1:
            os.system("clear")
            if login(user,db) == True:
                mg.menuGeneral(user,db)

        elif op == 2:
            os.system("clear")
            registrarse(user,db)

        elif op == 0:
            db.close()
            exit()
