package main

func main() {
	// // cards := newDeck()

	// // hand, remainingCards := deal(cards, 5)

	// // hand.print()
	// // remainingCards.print()

	// cards := newDeck()
	// cards.saveToFile("my_cards")

	cards := newDeck()
	cards.shuffle()
	cards.print()
}
