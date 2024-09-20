public class GradeCalculator {

    public static void main(String[] args) {
        // Scores for Alice, Bob, and Clive
        int[] aliceScores = {90, 60, 80};
        int[] bobScores = {50, 0, 30}; // Assuming absent is equivalent to 0
        int[] cliveScores = {60, 70, 75};

        // Calculate and print final grades
        System.out.println("Alice's final grade: " + calculateFinalGrade(aliceScores));
        System.out.println("Bob's final grade: " + calculateFinalGrade(bobScores));
        System.out.println("Clive's final grade: " + calculateFinalGrade(cliveScores));
    }

    // Method to calculate final grade based on scores
    private static String calculateFinalGrade(int[] scores) {
        int total = 0;
        for (int score : scores) {
            total += score;
        }
        double average = total / (double) scores.length;

        // Determine final grade based on average
        if (average > 80) {
            return "A";
        } else if (average > 60) {
            return "B";
        } else if (average > 40) {
            return "C";
        } else {
            return "D";
        }
    }
}
