public class RightAlignedTriangle {

    public static void main(String[] args) {
        int rows = 5; // Total number of rows in the pattern

        for (int i = 1; i <= rows; i++) {
            // Print spaces in decreasing order
            for (int j = rows - i; j > 0; j--) {
                System.out.print(" ");
            }
            // Print asterisks
            for (int k = 1; k <= i; k++) {
                System.out.print("*");
            }
            // Move to the next line
            System.out.println();
        }
    }
}
