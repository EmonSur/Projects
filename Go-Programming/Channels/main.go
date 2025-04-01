package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {
	links := []string{
		"http://amazon.com",
		"http://google.com",
		"http://facebook.com",
		"https://stackoverflow.com",
		"https://golang.org",
	}

	c := make(chan string) // how to create a new channel

	for _, link := range links {
		// we want to use goroutines to introduce concurrency - currently the code does the checklink code for each link one at a time
		// there is a wait in-betweeen each checklink, but we want the checklinks to happen at the same time
		go checkLink(link, c) // use simply 'go' to creata a go routine
		// go keyword is only used before function calls
		// this currently will not do anything as go has a main goroutine which checks if there is anything else to do, and if it doesn't find anything, it will stop.
		// these here are child goroutines, which are still running in the background, but are unable to finish due to the main goroutine
		// to fix this we will use the channels construct, which will help communicate between goroutines
	}

	// fmt.Println(<-c) // receive and log value from a channel
	// value received from a channel can also be assigned to a variable, e.g. myNumber <- channel
	// this currently only checks link to "http://google.com"

	for l := range c { // wait for c to return a value, and once it does so, assign it to some variable l
		go func() { // function literal
			time.Sleep(time.Second) // this will pause our main routine so a message would be received only every second
			// // if we want to have e.g. every 5 seconds, instead we would do 'time.Sleep(5 * time.Second)'
			checkLink(l, c)
		}() // need to have a '()' after a function literal to invoke/call it
	}
}

func checkLink(link string, c chan string) {
	_, err := http.Get(link)
	if err != nil {
		fmt.Println(link, "might be down!")
		c <- link // This send something into a channel
		return    // empty return to make sure we dont do anything else inside this function
	}

	fmt.Println(link, "is up!")
	c <- link
}
