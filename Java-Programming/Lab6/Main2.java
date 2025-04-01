

class Customer { // define a define a customer, with name, member, and member-type properties
    private String name; // private class members used to store name, member, and member-type (property values are the defaults)
    private boolean member = false;
    private String memberType;

    public Customer(String name) { // constuctor to create a customer with a name
        this.name = name;
    }

    public String getName() { // getter for name
        return name;
    }

    public boolean isMember() { // getter to see if ctomer is a member
        return member;
    }

    public void setMember(boolean member) { // setter for member status
        this.member = member;
    }

    public String getMemberType() { // getter for member-type
        return memberType;
    }

    public void setMemberType(String type) { // setter for member-type
        this.memberType = type;
    }

    @Override
    public String toString() { // method that will get string representation of a customer status
        String memberStr = isMember() ? ("Member Type: " + getMemberType()) : "Not a Member";
        return "Customer Name: " + getName() + ", " + memberStr;
    }
}

class Visit { // define a visit class, with customer, date and service/product expense as properties
    private Customer customer;  // private class members used to store customer, date, and service/expense 
    private java.util.Date date;
    private double serviceExpense;
    private double productExpense;

    public Visit(String name, java.util.Date date) { // constrcutor to create a visit for a customer on a particular date
        this.customer = new Customer(name);
        this.date = date;
    }

    public String getName() { // getter for name
        return customer.getName();
    }

    public double getServiceExpense() { // getter for service expense
        return serviceExpense;
    }

    public void setServiceExpense(double ex) { // setter for service expense
        serviceExpense = ex;
    }

    public double getProductExpense() { // getter for product expense
        return productExpense;
    }

    public void setProductExpense(double ex) { // setter for product expense
        productExpense = ex;
    }

    public double getTotalExpense() { // getter that will get (caculate and return) toal expense
        return serviceExpense + productExpense;
    }

    @Override
    public String toString() { // this will get the string representation of the customer's visit
        return "Visit for " + customer.getName() +
               "\nDate of Service: " + date +
               "\nService Expense Before Discount: " + serviceExpense +
               "\nProduct Expense Before Discount: " + productExpense;
    }
}

class DiscountRate { // class to the hold the different discount rates for the different types of member
    static double serviceDiscountPremium = 0.2; // static variables to hold discount for different member types
    static double serviceDiscountGold = 0.15;
    static double serviceDiscountSilver = 0.1;
    static double productDiscountPremium = 0.1;
    static double productDiscountGold = 0.1;
    static double productDiscountSilver = 0.1;

    public static double getServiceDiscountRate(String type) { // method to retrieve the service discount, based on the member type
        switch (type) {
            case "Premium":
                return serviceDiscountPremium;
            case "Gold":
                return serviceDiscountGold;
            case "Silver":
                return serviceDiscountSilver;
            default:
                return 0;
        }
    }

    public static double getProductDiscountRate(String type) { // method to retrieve the product discount based on the member type
        switch (type) {
            case "Premium":
                return productDiscountPremium;
            case "Gold":
                return productDiscountGold;
            case "Silver":
                return productDiscountSilver;
            default:
                return 0;
        }
    }
}

public class Main { // main class that contains the method to test out the customer, visit, and discount classes
    public static void main(String[] args) {
        // Create a customer with a Gold membership
        Customer customer = new Customer("John Doe");
        customer.setMember(true);
        customer.setMemberType("Gold");

        // Create a visit for the customer on today's date
        Visit visit = new Visit(customer.getName(), new java.util.Date());
        visit.setProductExpense(200.0);
        visit.setServiceExpense(50.0);

        // Apply discounts
        double totalServiceExpense = visit.getServiceExpense() - (visit.getServiceExpense() * DiscountRate.getServiceDiscountRate(customer.getMemberType()));
        double totalProductExpense = visit.getProductExpense() - (visit.getProductExpense() * DiscountRate.getProductDiscountRate(customer.getMemberType()));

        System.out.println("Invoice for the Visit:");
        System.out.println(visit);
        System.out.println("Service Expense After Discount: " + String.format("%.2f", totalServiceExpense));
        System.out.println("Product Expense After Discount: " + String.format("%.2f", totalProductExpense));
        System.out.println("Total Expense After Discount: " + String.format("%.2f", (totalServiceExpense + totalProductExpense)));
    }
}
