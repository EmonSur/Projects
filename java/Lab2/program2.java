public class CircleProperties {
    public static void main(String[] args) {
        // Given radius
        double radius = 181.55;
        
        // Constant PI
        final double PI = 3.14;

        // Compute area of the circle
        double area = PI * radius * radius;

        // Compute circumference of the circle
        double circumference = 2 * PI * radius;

        // Output the computed properties
        System.out.println("Area of the circle: " + area + " square units");
        System.out.println("Circumference of the circle: " + circumference + " units");
    }
}
