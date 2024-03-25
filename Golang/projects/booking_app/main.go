package main

import (
	"fmt"
	"sync"
	"time"
)

// one can add a colon to a variable, but not a const or a var
var conferenceName = "Go conference"

// const tells Go that the value is not allowed to change
const conferenceTickets int = 50

var remainingTickets uint = 10

// slice
var bookings = make([]UserData, 0)

type UserData struct {
	firstName       string
	lastName        string
	email           string
	numberOfTickets uint
}

var wg = sync.WaitGroup{}

func main() {
	// call the greetUsers function
	greetUsers()

	firstName, lastName, email, userTicket := getUserInput()
	isValidName, isValidEmail, isValidTicketNumber := ValidateUserInput(firstName, lastName, email, userTicket, remainingTickets)

	if isValidName && isValidEmail && isValidTicketNumber {

		bookTicket(userTicket, firstName, lastName, email)

		wg.Add(1)
		go sendTicket(userTicket, firstName, lastName, email)

		// Print first names
		firstNames := getFirstNames()
		fmt.Printf("The first names of bookings are: %v\n", firstNames)

		if remainingTickets == 0 {
			// end the program
			fmt.Println("Our conference is booked out, Come back next year.")
			//break

		}
	} else {
		if !isValidEmail {
			fmt.Println("first name or last name you entered is too short.")
		}

		if !isValidEmail {
			fmt.Println("email address you entered does not contain @ sign")
		}
		if !isValidTicketNumber {
			fmt.Println("number of tickets entered is invalid")
		}
	}
	wg.Wait()
}

func greetUsers() {
	fmt.Printf("Welcome to %v booking application.\n", conferenceName)
	fmt.Printf("We have a total of %v tickets and %v are still available.\n", conferenceTickets, remainingTickets)
	fmt.Println("Get your tickets here to attend")
}

func getFirstNames() []string {
	// slice for first names in the form of strings
	firstNames := []string{}
	for _, booking := range bookings {
		firstNames = append(firstNames, booking.firstName)
	}

	return firstNames
}

func getUserInput() (string, string, string, uint) {

	var firstName string
	var lastName string
	var email string
	var userTicket uint
	// ask user for their name
	// pointer will print out the memory address of the stored variable
	fmt.Println("Enter your first name: ")
	fmt.Scan(&firstName)

	fmt.Println("Enter your last name: ")
	fmt.Scan(&lastName)

	fmt.Println("Enter your email: ")
	fmt.Scan(&email)

	fmt.Println("Enter number of tickets: ")
	fmt.Scan(&userTicket)

	return firstName, lastName, email, userTicket

}

func bookTicket(userTicket uint, firstName string, lastName string, email string) {
	remainingTickets = remainingTickets - userTicket

	// create a map for a user
	var userData = UserData{
		firstName:       firstName,
		lastName:        lastName,
		email:           email,
		numberOfTickets: userTicket,
	}

	bookings = append(bookings, userData)
	fmt.Printf("List of bookings is %v\n", bookings)

	//userTicket = 2
	fmt.Printf("Thank you, %v %v for booking %v tickets. You will receive a confirmation email at %v.\n", firstName, lastName, userTicket, email)
	fmt.Printf("%v tickets remaining for %v\n", remainingTickets, conferenceName)
}

func sendTicket(userTickets uint, firstName string, lastName string, email string) {
	time.Sleep(50 * time.Second)
	var ticket = fmt.Sprintf("%v tickets for %v %v", userTickets, firstName, lastName)
	fmt.Println("############")
	fmt.Printf("Sending ticket:\n %v \nto email address %v\n", ticket, email)
	fmt.Println("############")
	wg.Done()
}
