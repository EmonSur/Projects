import java.util.Scanner;

public class EvenOddCounter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int evenCount = 0; 
        int oddCount = 0; 

        System.out.println("Please enter in 10 numbers:");

        for (int i = 1; i <= 10; i++) {
            System.out.print("Number " + i + ": ");
            int number = scanner.nextInt();

            if (number % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }

        System.out.println("Total even numbers: " + evenCount);
        System.out.println("Total odd numbers: " + oddCount);
    }
}
