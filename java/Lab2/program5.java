public class LoanCalculator {

    public static void main(String[] args) {
        // Monthly incomes of Alice, Bob, and Clive
        int aliceIncome = 1500;
        int bobIncome = 700;
        int cliveIncome = 100;

        // Calculate and print loan category and amount
        printLoanDetails("Alice", aliceIncome);
        printLoanDetails("Bob", bobIncome);
        printLoanDetails("Clive", cliveIncome);
    }

    // Method to determine loan category and calculate loan amount
    private static void printLoanDetails(String name, int monthlyIncome) {
        int category;
        double loanAmount;

        // Determine loan category based on monthly income
        if (monthlyIncome > 1000) {
            category = 1;
        } else if (monthlyIncome > 500) {
            category = 2;
        } else if (monthlyIncome > 200) {
            category = 3;
        } else {
            category = 4;
        }

        // Calculate loan amount based on category
        switch (category) {
            case 1:
                loanAmount = 3.5 * monthlyIncome * 12;
                break;
            case 2:
                loanAmount = 2.5 * monthlyIncome * 12;
                break;
            case 3:
                loanAmount = 2 * monthlyIncome * 12;
                break;
            default:
                loanAmount = 0; // No loan for category 4
                break;
        }

        // Output loan details
        System.out.println(name + "'s loan category: " + category + " and loan amount: " + loanAmount + " euros.");
    }
}
