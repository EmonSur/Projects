// import the following classes to create arrays, sort, and read input from the user
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class Subjects { //define a public class to organise the subjects in the computer science dept

    public static void main(String[] args) { //main method of program
        Scanner scanner = new Scanner(System.in); //create a scanner that will allow for input to be read
        ArrayList<String> subjects = new ArrayList<>(); //initialise an array to store input

        //ask the user to enter the 4 subjects referenced that are taught in the computer science dept
        System.out.println("Enter the subjects taught in the computer science department:");
        for (int i = 0; i < 4; i++) { //loop to collect 4 inputs
            System.out.print("Subject " + (i + 1) + ": ");
            subjects.add(scanner.nextLine());
        }

        //remove the subject 'Networking' (nothing will happen if it is not inputted )
        subjects.remove("Networking");

        //sort the array in reverse alphabetical order
        Collections.sort(subjects, Collections.reverseOrder());

        //print a message and then list's contents
        System.out.println("Here are the remaining subjects in reverse alphabetical order:");
        for (String subject : subjects) {
            System.out.println(subject);
        }
    }
}
