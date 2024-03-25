package main

import "fmt"

func main(){

	messagesFromDoris := []string{
		"You doing anything later??",
		"Did you get my last message?",
	}
	numMessages := float64(len(messagesFromDoris))
	costPerMessage := .02

	// do not touch this line

	totalCost := costPerMessage * numMessages

	// do not touch this line

	fmt.Printf("Doris spent %.2f on text messages today\n", totalCost)
}
