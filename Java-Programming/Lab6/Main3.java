class Circle { // 9define circle class, with radius and colour properties
    private double radius = 1.0; // private class members used to store colour and radius (property values are the defaults)
    private String colour = "red";

    public Circle() { // a no-arguement constructor, where the properties of the class are set to the defaults

       }

    public Circle(double radius) { // constructor that sets radius and height
        this.radius = radius;
    }

    public Circle(double radius, String colour) { // constructor that sets radius and colour 
        this.radius = radius;
        this.colour = colour;
    }

    public double getRadius() { // getter for radius
        return radius;
    }

    public void setRadius(double radius) { // setter for radius
        this.radius = radius;
    }

    public String getColour() { // getter for colour
        return colour;
    }

    public void setColour(String colour) { // setter for colour
        this.colour = colour;
    }

    public double getArea() { // getter that will get (calculate and return) area of circle
        return Math.PI * radius * radius;
    }

    public String toString() { // method that will get string representation of a circle
        return "Circle[radius=" + radius + ", colour=" + colour + "]";
    }
}


class Cylinder extends Circle { // defines the class cylinder that extends (inherits off of) circle class
    private double height = 1.0; // private class members used to store height (property values are the defaults)


    public Cylinder() { // a no-arguement constructor, where the properties of the class are set to the defaults
    }

    public Cylinder(double radius) { // constructor that the radius (inherited from super)
        super(radius);
    }

    public Cylinder(double radius, double height) { // constructor that sets height and the radius (inherited from super)
        super(radius);
	this.height = height;
    }

    public Cylinder(double radius, double height,  String colour) { // constructor that sets height, and both colour and radius (both inherited from super class)
        super(radius, colour);
	this.height = height;
    }

    public double getHeight() { // getter for height
        return height;
    }

    public void setHeight(double height) { // setter for height
        this.height = height;
    }

    @Override // this will override supers getArea() method
    public double getArea() { 
        // Surface area of the cylinder (2πrh + 2πr^2)
        return (2 * Math.PI * getRadius() * height) + (2 * super.getArea());
    }

    public double getVolume() { // getter that will get(calculate and return) volume
        // Volume of the cylinder (πr^2h)
        return super.getArea() * height;
    }

    @Override // this will override supers string representation, and use cylinder's
    public String toString() {
	return "Cylinder[" + super.toString() + " and height=" + height;
    }
}



public class Main { // main class that will contain the method that will be used to test the different classes
    public static void main(String[] args) {
        Circle circle = new Circle(5, "blue");
        Cylinder cylinder = new Cylinder(5, 10, "blue");

        System.out.println(circle); // test circle class
        System.out.println("Area of the circle: " + circle.getArea());

        System.out.println(cylinder); // test cylinder class
        System.out.println("Surface area of the cylinder: " + cylinder.getArea());
        System.out.println("Volume of the cylinder: " + cylinder.getVolume());

        }
}
