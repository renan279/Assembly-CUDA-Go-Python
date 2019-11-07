package main

import (
	"fmt" //pode-se usar ."fmt" para na hora de usar suas funções, não utilizar sua biblioteca
	"time"
)

func soma(x, y int) int { //oooo tipo das funções e variáveis ficam depois da declaração
	return x + y //x e y são int, mas pode-se declarar apenas a ultima que será atribuido para as anteriores
}

func alternar(string1, string2 string) (string, string) {
	return string2, string1
}

func main() {
	start := time.Now() //atribui o tempo atual ao start

	fmt.Println(soma(2, 4))

	fmt.Println("alternar strings")
	a, b := alternar("hello", "world")
	fmt.Println(a, b)

	num := 10
	fmt.Printf("funciona como em C, %d", num)
	fmt.Print("Print na linha, sem pular\n")

	fmt.Println(time.Since(start)) //conta o tempo de start até esse momento
}
