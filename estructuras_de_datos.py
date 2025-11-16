#ESTRUCTURAS DE DATOS O COLECCIONES
#Listas
#tiene la capacidad de guardar varios elementos, inclusive de distintos tipos
list_3 = [1,2,3,4,5]

list_1 = [
    "bacon",
    "eggs",
    "cheese",
    12,
    True,
    list_3
]

list_2 = [
    "banana",
    "spaguetti",
    "kiwi",
    "mango"
]



#diccionarios
#Esta compuesto de dos partes: indice y valor (tambien puede almacenar listas)
dictionary_1 = {
    "Computer program": "A series of instructions that can be executed by a computer",
    "Syntax": "The rules we create for computers and programmers to follow to avoid ambiguity and give strict meanings",
    "Programming Language": "A formal set of syntax for writing a computer program",
    "list_2": list_1
}

#Pueden tener listas dentro del diccionario
dictionary_2 = {
  "pilot": "James",
  "co-pilot": "Paul",
  "stewards": [
    "Peter",
    "Carol",
    "Jane"
  ],
  "breakfast": list_2,
  "passengers": 203
}
