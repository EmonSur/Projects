class Customer {
    private String name;
    private boolean member = false;
    private String memberType;

    public Customer(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public boolean isMember() {
        return member;
    }

    public void setMember(boolean member) {
        this.member = member;
    }

    public String getMemberType() {
        return memberType;
    }

    public void setMemberType(String type) {
        this.memberType = type;
    }

    public String toString() {
        return "Customer[name=" + name + ",member=" + member + ",memberType=" + memberType + "]";
    }
}

class Visit {
    private Customer customer;
    private java.util.Date date;
    private double serviceExpense;
    private double productExpense;

    public Visit(String name, java.util.Date date) {
        this.customer = new Customer(name);
        this.date = date;
    }

    public String getName() {
        return customer.getName();
    }

    public double getServiceExpense() {
        return serviceExpense;
    }

    public void setServiceExpense(double ex) {
        serviceExpense = ex;
    }

    public double getProductExpense() {
        return productExpense;
    }

    public void setProductExpense(double ex) {
        productExpense = ex;
    }

    public double getTotalExpense() {
        return serviceExpense + productExpense;
    }

    public String toString() {
        return "Visit[customer=" + customer + ",date=" + date + ",serviceExpense=" + serviceExpense + ",productExpense=" + productExpense + "]";
    }
}

class DiscountRate {
    static double serviceDiscountPremium = 0.2;
    static double serviceDiscountGold = 0.15;
    static double serviceDiscountSilver = 0.1;
    static double productDiscountPremium = 0.1;
    static double productDiscountGold = 0.1;
    static double productDiscountSilver = 0.1;

    public static double getServiceDiscountRate(String type) {
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

    public static double getProductDiscountRate(String type) {
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

public class Main {
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

        // Print the total expense
        System.out.println("Total service expense after discount: " + totalServiceExpense);
        System.out.println("Total product expense after discount: " + totalProductExpense);
        System.out.println("Total expense after discount: " + (totalServiceExpense + totalProductExpense));
    }
}
