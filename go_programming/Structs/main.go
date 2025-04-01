package main

import "fmt"

type contactInfo struct {
	email   string
	zipCode int
}

type person struct {
	firstName   string
	lastName    string
	contactInfo // equivalent to contactInfo contactInfo (called contactInfo and is type contactInfo)
}

func main() {
	jim := person{
		firstName: "Jim",
		lastName:  "Anderson",
		contactInfo: contactInfo{
			email:   "Jim94@gmail.com",
			zipCode: 78192,
		},
	}

	// jimPointer := &jim // Address of jim /pointer to jim
	// // & turns a value into an address
	// jimPointer.updateName("Jimmy")
	jim.updateName("Jimmy")
	// Go also automatically turns your type of person to pointer to person for you
	jim.print()
}

func (pointerToPerson *person /*pointer*/) updateName(newFirstName string) {
	(*pointerToPerson).firstName = newFirstName
	// Where there is a * where a type should be, it means this is a type description.
	// *pointerToPerson is an operator, meaning we want to manipulate the value the pointer is referencing
	// * turns an address to a value
}

func (p person) print() {
	fmt.Println("%+v", p)
}
