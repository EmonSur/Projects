import java.util.Scanner;

public class CoffeeSaleCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt for and read the unit weight of a bag of coffee
        System.out.print("Enter the weight per bag in pounds: ");
        double unitWeight = scanner.nextDouble();

        // Prompt for and read the number of bags sold
        System.out.print("Enter the number of bags sold: ");
        int numberOfBags = scanner.nextInt();

        // Constants for price per pound and sales tax
        final double pricePerPound = 5.99;
        final double salesTaxRate = 0.0725;

        // Calculate total price
        double totalPrice = unitWeight * numberOfBags * pricePerPound;
        double totalPriceWithTax = totalPrice + totalPrice * salesTaxRate;

        // Display the results
        System.out.println("Number of bags sold: " + numberOfBags);
        System.out.println("Weight per bag: " + unitWeight + " lb");
        System.out.println("Price per pound: $" + pricePerPound);
        System.out.printf("Sales tax: %.2f%%\n", salesTaxRate * 100);
        System.out.printf("Total price: $ %.3f\n", totalPriceWithTax);
    }
}
