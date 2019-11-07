package main

import (
	"fmt"
)

func main() {

	for i := 0; i < 10; i++ { //tradicional for
		fmt.Printf("Hello %d\n", i)
	}

	count := 0
	for count < 10 { // while
		fmt.Printf("Hello World %d\n", count)
		count++
	}

}
