import java.util.Scanner;

public class PerfectNumberChecker {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt for and read the number
        System.out.print("Enter a number between 20 and 30: ");
        int number = scanner.nextInt();

        // Check if the number is within the specified range
        if (number < 20 || number > 30) {
            System.out.println("Number is not in the range of 20 to 30.");
            return;
        }

        // Find and display the proper divisors
        System.out.print("Proper divisors of " + number + ": ");
        int sumOfDivisors = 0;
        for (int i = 1; i <= number / 2; i++) {
            if (number % i == 0) {
                sumOfDivisors += i;
                System.out.print(i + " ");
            }
        }
        System.out.println(); // Move to the next line

        // Determine and display if the number is perfect
        if (sumOfDivisors == number) {
            System.out.println(number + " is a perfect number.");
        } else {
            System.out.println(number + " is not a perfect number.");
        }
    }
}
