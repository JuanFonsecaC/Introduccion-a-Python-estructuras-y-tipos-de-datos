package main

import "fmt"

func main() {
    fmt.Println("¡Hola Mundo!")
    
    var edad int
    fmt.Scanln(&edad)

    if edad >= 18 {
        fmt.Println("Es mayor de edad")
    } else {
        fmt.Println("Es menor de edad")
    }
}
