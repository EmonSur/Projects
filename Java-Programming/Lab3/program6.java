import java.util.Scanner;

public class DiamondPattern {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Prompt for and read the number of rows for the diamond's half
        System.out.print("Enter number of rows for the diamond's half: ");
        int rows = scanner.nextInt();

        // Upper half of the diamond
        for (int i = 1; i <= rows; i++) {
            // Print leading spaces
            for (int j = rows; j > i; j--) {
                System.out.print(" ");
            }
            // Print asterisks
            for (int k = 1; k < (i * 2); k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Lower half of the diamond
        for (int i = rows - 1; i > 0; i--) {
            // Print leading spaces
            for (int j = rows; j > i; j--) {
                System.out.print(" ");
            }
            // Print asterisks
            for (int k = 1; k < (i * 2); k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
