class Shape { //define shape class with colour and filled properties
    private String colour = "red"; //private class members used to store colour and filled status
    private boolean filled = true;

    public Shape() { //a no-arguement constructor, where the properties of the class are set to the defaults
    }

    public Shape(String colour, boolean filled) { //constructor that sets the colour and filled
        this.colour = colour;
        this.filled = filled;
    }

    public String getColour() { //getter for colour
        return colour;
    }

    public void setColour(String colour) { //setter for colour
        this.colour = colour;
    }

    public boolean isFilled() { //getter for filled
        return filled;
    }

    public void setFilled(boolean filled) { //setter for filled
        this.filled = filled;
    }

    public String toString() { //method that will get the string representation of the shape
        return "Shape[colour=" + colour + ",filled=" + filled + "]";
    }
}

class Circle extends Shape { //defines the class circle that extends (inherits of) shape class
    private double radius = 1.0; //private class member

    public Circle() { //a no-arguement constructor, where the properties of the class are set to the defaults
    }

    public Circle(double radius) { //constructor that sets radius
        this.radius = radius;
    }

    public Circle(double radius, String colour, boolean filled) { //constrcutor that sets radius, and the colour and filled (both inherited from super class)
        super(colour, filled);
        this.radius = radius;
    }

    public double getRadius() { //getter for radius
        return radius;
    }

    public void setRadius(double radius) { //setter for radius
        this.radius = radius;
    }

    public double getArea() { //getter that will get (calculate and return) area of circle
        return Math.PI * radius * radius;
    }

    public double getPerimeter() { //getter that will get (calculate and return) perimeter of circle
        return 2 * Math.PI * radius;
    }

    @Override //this will override and use string representation of the super class and use circle class's instead
    public String toString() { //method that will get a string representation of the circle
 	return "Circle[" + super.toString() + ",radius=" + radius + "]";
    }
}

class Rectangle extends Shape { //defines rectangle class, which extends (inherits) shape class
    private double width = 1.0; //private class members for width and length of rectangle
    private double length = 1.0;

    public Rectangle() { //a no-arguement constructor, where the properties of the class are set to the defaults
    }

    public Rectangle(double width, double length) { //constructor that will set length and width properties
        this.width = width;
        this.length = length;
    }

    public Rectangle(double width, double length, String colour, boolean filled) { //constructor that will set length and width properties, alongside colour and filled properties, inherited from super class
        super(colour, filled);
        this.width = width;
        this.length = length;
    }

    public double getWidth() { //getter for width
        return width;
    }

    public void setWidth(double width) { //setter for width
        this.width = width;
    }

    public double getLength() { //getter for length
        return length;
    }

    public void setLength(double length) { //setter for length
        this.length = length;
    }

    public double getArea() { //getter that will get (calculate and returm) area
        return width * length;
    }

    public double getPerimeter() { //getter that will get(calculate and return) perimetre
        return 2 * (width + length);
    }

    @Override //will override string representation of super class, and will instead use rectangle class's
    public String toString() {
	return "Rectangle[" + super.toString() + ",width=" + width + ",length=" + length + "]";
    }
}

class Square extends Rectangle { //define the square class, that inherits from the rectangle class
    public Square() {
    }

    public Square(double side) { //a no-arguement constructor, where the properties of the class are set to the defaults (in this case length=width=side)
        super(side, side);
    }

    public Square(double side, String colour, boolean filled) { //constructor that will set the side properties, alongside the colour and filled properties that will be inherited from the super's super
        super(side, side, colour, filled);
    }

    public double getSide() { //getter for side
        return getWidth();
    }

    public void setSide(double side) { //setter for side
        super.setWidth(side);
        super.setLength(side);
    }

    @Override //this will override supers width setter
    public void setWidth(double width) { //setter for width
        setSide(width);
    }

    @Override //this will override supers length setter
    public void setLength(double length) { //setter for length
        setSide(length);
    }

    @Override //will override supers string representation and will use square's instead
    public String toString() { 
	return "Square[" + super.toString().replace("Rectangle", "Shape") + "]";
    }
}

class Main { //main class that will contain the method that will be used to test the different classes
    public static void main(String[] args) {

	Shape shape = new Shape("purple", false); //test ths shape class
        System.out.println(shape);

        Circle circle = new Circle(5, "blue", false); //test the circle class
        System.out.println(circle);
        System.out.println("Area of circle: " + circle.getArea());
        System.out.println("Perimeter of circle: " + circle.getPerimeter());

        Rectangle rectangle = new Rectangle(4, 5, "red", true); //test the rectangle class
        System.out.println(rectangle);
        System.out.println("Area of rectangle: " + rectangle.getArea());
        System.out.println("Perimeter of rectangle: " + rectangle.getPerimeter());

        Square square = new Square(4, "yellow", true); //test the square class
        System.out.println(square);
        System.out.println("Area of square: " + square.getArea());
        System.out.println("Perimeter of square: " + square.getPerimeter());
    }
}



