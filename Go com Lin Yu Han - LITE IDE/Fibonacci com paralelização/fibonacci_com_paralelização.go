package main

import (
	"fmt"
	"time"
	"runtime"
)

func fibonacci(num int) int {
	if num == 0 || num == 1 {
		return 1
	} else {
		return fibonacci(num-1) + fibonacci(num-2)
	}
}

func main() {
	c := make(chan int)
	runtime.GOMAXPROCS(runtime.NumCPU())
	
	qtdNum := 10 //qtd de números
	start := time.Now()
	for i := 0; i < qtdNum; i++ {
		c <- go fibonacci(i + 1)
	}
	
	for i := 0; i < qtdNum; i++ {
		fmt.Println( <- c)
	}

	fmt.Println(time.Since(start)) //tempo que leva para calcular o fibonacci
}
