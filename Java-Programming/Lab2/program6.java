public class BloodDonationEligibility {

    public static void main(String[] args) {
        // Details of Alice, Bob, Jemmy, and Clive
        checkEligibility("Alice", 50, 19);
        checkEligibility("Bob", 36, 20);
        checkEligibility("Jemmy", 45, 17);
        checkEligibility("Clive", 100, 80);
    }

    // Method to check eligibility for blood donation
    private static void checkEligibility(String name, int weight, int age) {
        String message = name + " can donate blood.";
        if (age < 18 || age > 60) {
            message = name + " cannot donate blood because of age restrictions.";
        } else if (weight <= 40) {
            message = name + " cannot donate blood because their weight is too low.";
        }

        System.out.println(message);
    }
}
