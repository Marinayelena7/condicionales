#Escribe un programa que le pida al usuario ingresar un nombre de usuario y una contraseña. Si el nombre de usuario es "admin" y la contraseña es "1234", el programa debe mostrar "Acceso concedido". Si no, debe mostrar "Acceso denegado". Este tipo de programa se utiliza en muchos sitios web y sistemas para controlar el acceso. 
print("Escriba su nombre de usuario")
usuario = input()
print("Escriba su contraseña")
contraseña = int(input())
if(usuario =="admin" and contraseña ==1234):
        print("Acceso concedido")
else: print("Acceso denegado")
