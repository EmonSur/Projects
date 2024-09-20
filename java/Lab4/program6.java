import java.util.Scanner;
import java.util.Random;

public class MatrixSearch2D {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        // Create a 2D array (3x3 matrix)
        int[][] matrix = new int[3][3];
        
        // Populate the matrix with random integers and display it
        System.out.println("Generated 2D matrix:");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                // Assign a random integer from 0 to 9
                matrix[i][j] = random.nextInt(10);
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println(); // Move to the next line after each row
        }
        
        // Input a number from the user
        System.out.print("\nEnter a number to search for in the 2D matrix: ");
        int numberToFind = scanner.nextInt();
        
        // Check if the number is present in the 2D matrix
        boolean found = false;
        for (int i = 0; i < matrix.length && !found; i++) {
            for (int j = 0; j < matrix[i].length && !found; j++) {
                if (matrix[i][j] == numberToFind) {
                    found = true;
                }
            }
        }
        
        // Output the result
        if (found) {
            System.out.println("The number " + numberToFind + " is present in the matrix.");
        } else {
            System.out.println("The number " + numberToFind + " is not present in the matrix.");
        }
    }
}
