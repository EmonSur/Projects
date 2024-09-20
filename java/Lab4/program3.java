import java.util.Arrays;
import java.util.Scanner;

public class AlphabeticalNames {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] names = new String[10];

        // Input 10 names from the user
        System.out.println("Enter 10 names:");
        for (int i = 0; i < names.length; i++) {
            System.out.print("Name " + (i + 1) + ": ");
            names[i] = scanner.nextLine();
        }

        // Sort the names alphabetically
        Arrays.sort(names);

        // Print the sorted list of names
        System.out.println("Names in alphabetical order:");
        for (String name : names) {
            System.out.println(name);
        }
    }
}
