import java.util.Scanner;

public class StudentGrades {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt for and read the number of students
        System.out.print("Enter the number of students in the class: ");
        int numberOfStudents = scanner.nextInt();
        scanner.nextLine(); // Consume the newline left by nextInt()

        String[] names = new String[numberOfStudents];
        int[] marks = new int[numberOfStudents];
        double totalMarks = 0;

        // Input name and marks for each student
        for (int i = 0; i < numberOfStudents; i++) {
            System.out.print("Enter name for student " + (i + 1) + ": ");
            names[i] = scanner.nextLine();

            System.out.print("Enter marks for " + names[i] + ": ");
            marks[i] = scanner.nextInt();
            scanner.nextLine(); // Consume the newline

            totalMarks += marks[i];
        }

        // Output name and grade for each student
        System.out.println("Student Grades:");
        for (int i = 0; i < numberOfStudents; i++) {
            System.out.println(names[i] + ": " + getGrade(marks[i]));
        }

        // Calculate and output the average marks of the class
        double averageMarks = totalMarks / numberOfStudents;
        System.out.printf("Average marks of the class: %.2f\n", averageMarks);
    }

    // Method to determine the grade based on marks
    private static String getGrade(int marks) {
        if (marks > 80) {
            return "A";
        } else if (marks > 60) {
            return "B";
        } else if (marks > 40) {
            return "C";
        } else {
            return "D";
        }
    }
}
