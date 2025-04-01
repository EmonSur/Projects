package main

import "fmt"

func main() {

	// Method 1:
	// var colours map[string]string //map[keys of type string]values of type string

	// Method 2:
	// colours := make(map[int]string)

	// colours[10] = "#ffffff"

	// delete(colours, 10) // Delete a key/value pair from a map

	// Method 3:
	colours := map[string]string{
		"red":   "#ff0000",
		"green": "#4bf745",
		"white": "#ffffff",
	}

	printMap(colours)
}

func printMap(c map[string]string) {
	for colour, hex := range c {
		fmt.Println("Hex code for the given colour", colour, "is", hex)
	}
}

// Notes:
// All keys must be of the same type, and values need to be of the same type. This is not the case in structs.
// All key-value pairs are indexed, so we can iterate through all the pairs in it. Not the case for structs.
// Use a map when creating a collection of closely related properties. If you have a closed set of keys, maybe use a struct.
