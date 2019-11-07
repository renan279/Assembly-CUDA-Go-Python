package main

import (
	"fmt"
	"time"
)

func fibonacci(num int) int {
	if num == 0 || num == 1 {
		return 1
	} else {
		return fibonacci(num-1) + fibonacci(num-2)
	}
}

func main() {
	qtdNum := 10 //qtd de números
	start := time.Now()
	for i := 0; i < qtdNum; i++ {
		fmt.Println(fibonacci(i + 1))
	}
	fmt.Println(time.Since(start)) //tempo que leva para calcular o fibonacci
}
