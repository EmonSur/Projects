package main

import "fmt"

// Means basically we have a new 3rd type 'bot'
type bot interface {
	// If you are a type with a function called 'getGreeting()' and you return a string
	// Then you are an 'honourary member' of type 'bot'
	getGreeting() string
	// In brckets we say arguement types, and after brackets we say return types
}

type englishBot struct{}

type spanishBot struct{}

func main() {

	eb := englishBot{}
	sb := spanishBot{}

	printGreeting(eb)
	printGreeting(sb)
}

// Now that you are a 'honorary member' of type bot, you can use call the function printGreeting()
func printGreeting(b bot) {
	fmt.Println(b.getGreeting())
}

func (englishBot) getGreeting() string {
	// VERY custom logic for generating an english greeting
	return "Hi there!"
}

func (spanishBot) getGreeting() string {
	// VERY custom logic for generating an spanish greeting
	return "Hola!"
}
