import java.util.Scanner; //import scanner class to get input from the user

public class StringOperations { //define a public class that will organise user inputted strings
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); //create a scanner that will allow to take input from user
        System.out.print("Input 1 from User: ");
        String firstString = scanner.nextLine();
        System.out.print("Input 2 from User: ");
        String secondString = scanner.nextLine();

        String concatenatedString = firstString + " " + secondString; //concatenate the 2 strings together and print to console
        System.out.println("Output 1: " + concatenatedString);

        String withoutSpaces = concatenatedString.replace(" ", "").toLowerCase(); //now to get the number of characters in the strings we will first remove all spaces, then use length() to get no. of charactesr
        System.out.println("Output 2: " + withoutSpaces.length());

        String[] words = concatenatedString.split(" "); //split the concatenated string into words
        String reversedOrderWords = ""; //iterate over the list from the end, and add these words into a list of reversed words
        for (int i = words.length - 1; i >= 0; i--) {
            reversedOrderWords += words[i];
            if (i > 0) {
                reversedOrderWords += " "; //add space between words
            }
        }
        System.out.println("Output 3: " + reversedOrderWords);

        int[] charFrequencies = new int[256]; //create an array that will count the frequency of each character
        for (char c : withoutSpaces.toCharArray()) { //iterate over each character in the strings (exluding spaces)
            charFrequencies[c]++; //add to frequency 
        }

        System.out.print("Output 4: "); //print the characters that have a frequency of exactly 2
        for (int i = 0; i < charFrequencies.length; i++) {
            if (charFrequencies[i] == 2) {
                System.out.print((char) i);
            }
        }
    }
}


