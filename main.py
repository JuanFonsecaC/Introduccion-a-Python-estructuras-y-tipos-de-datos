#PROGRAMA QUE MUESTRA NOMBRE Y APELLIDO
print("¿What is your first name?") #imprime en la consola "¿What is your first name?"
first_name = input("Write here:") #almaceno el nombre en la variable first_name, y muestro el texto "write here"
print("¿What is your last name?") #imprime en la consola "¿What is your last name?"
last_name = input("Write here:") #almaceno el apellido en la variable last_name, y muestro el texto "write here"
print("Hey " + first_name + " " + last_name + "!") #imprime en la consola "Hey" y concatena con el signo + las variables y el texto restante "!"
print("Hey",first_name,last_name,"!") #imprime en la consola "Hey" y concatena con el signo ,(OJO LA COMA AGREGA ESPACIO) las variables y el texto restante "!"
print(f"Hey {first_name} {last_name}!")#imprime en la consola "Hey" mediante transpolacion de strings(IMPORTANTE LA F AL PRINCIPIO), las variables y el texto restante "!"
