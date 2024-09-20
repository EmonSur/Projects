import java.util.ArrayList;
import java.util.List;

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "(" + x + "," + y + ")";
    }
}

class Polyline {
    private List<Point> points;

    public Polyline() {
        this.points = new ArrayList<>();
    }

    public void appendPoint(int x, int y) {
        Point newPoint = new Point(x, y);
        points.add(newPoint);
    }

    public void appendPoint(Point point) {
        points.add(point);
    }

    public double getLength() {
        double length = 0;
        for (int i = 0; i < points.size() - 1; i++) {
            Point start = points.get(i);
            Point end = points.get(i + 1);
            length += Math.hypot(end.x - start.x, end.y - start.y);
        }
        return length;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("{");
        for (Point point : points) {
            sb.append(point);
        }
        sb.append("}");
        return sb.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        Polyline polyline = new Polyline();
        polyline.appendPoint(1, 1);
        polyline.appendPoint(2, 3);
        polyline.appendPoint(3, 0);

        System.out.println("Polyline: " + polyline);
        System.out.println("Length of Polyline: " + polyline.getLength());
    }
}


