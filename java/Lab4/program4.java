import java.util.Scanner;

public class MatrixAddition {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] firstMatrix = new int[3][3];
        int[][] secondMatrix = new int[3][3];
        int[][] sumMatrix = new int[3][3];

        // Input for the first matrix
        System.out.println("Enter the elements for the first 3x3 matrix:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                firstMatrix[i][j] = scanner.nextInt();
            }
        }

        // Input for the second matrix
        System.out.println("Enter the elements for the second 3x3 matrix:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                secondMatrix[i][j] = scanner.nextInt();
            }
        }

        // Adding the two matrices
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                sumMatrix[i][j] = firstMatrix[i][j] + secondMatrix[i][j];
            }
        }

        // Displaying the result
        System.out.println("Sum of the two matrices is:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(sumMatrix[i][j] + " ");
            }
            System.out.println(); // To move to the next row
        }
    }
}
