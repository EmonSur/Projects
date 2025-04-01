public class WeightCalculator {
    public static void main(String[] args) {
        // Alice's weight on Earth (in kg)
        double earthWeight = 50.0;

        // Multipliers for weight on different planets
        double mercuryMultiplier = 0.4;
        double venusMultiplier = 0.9;
        double jupiterMultiplier = 2.5;
        double saturnMultiplier = 1.1;

        // Calculate weight on different planets
        double mercuryWeight = earthWeight * mercuryMultiplier;
        double venusWeight = earthWeight * venusMultiplier;
        double jupiterWeight = earthWeight * jupiterMultiplier;
        double saturnWeight = earthWeight * saturnMultiplier;

        // Output Alice's weight on different planets
        System.out.println("Alice's weight on Mercury: " + mercuryWeight + " kg");
        System.out.println("Alice's weight on Venus: " + venusWeight + " kg");
        System.out.println("Alice's weight on Jupiter: " + jupiterWeight + " kg");
        System.out.println("Alice's weight on Saturn: " + saturnWeight + " kg");
    }
}
