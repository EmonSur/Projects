import java.util.Scanner;

public class StandardDeviationCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Ask the user for the number of elements N
        System.out.print("Enter the number of elements N: ");
        int N = scanner.nextInt();
        
        double[] numbers = new double[N];
        double sum = 0;

        // Read N real numbers
        System.out.println("Enter " + N + " real numbers:");
        for (int i = 0; i < N; i++) {
            numbers[i] = scanner.nextDouble();
            sum += numbers[i];
        }
        
        // Calculate the mean (average)
        double mean = sum / N;
        
        // Calculate the sum of the squared differences from the mean
        double sumOfSquaredDifferences = 0;
        for (double num : numbers) {
            sumOfSquaredDifferences += Math.pow(num - mean, 2);
        }
        
        // Calculate standard deviation
        double standardDeviation = Math.sqrt(sumOfSquaredDifferences / N);
        
        // Output the result
        System.out.println("The standard deviation is: " + standardDeviation);
    }
}
