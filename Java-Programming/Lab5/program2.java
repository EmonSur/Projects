//import the following classes, to use hashmaps and to get input from user
import java.util.HashMap;
import java.util.Scanner;

public class RealMadridPlayers { //declare public class that will organise the (sum) of the real madrid players

    public static void main(String[] args) { //declare main method
        Scanner scanner = new Scanner(System.in); //create a scanner which will read input from user
        HashMap<Integer, String> players = new HashMap<>(); //initialise the hashmap

        players.put(1, "Thibaut Courtois"); //add the players and jersey numbers of (some) the real madrid players
        players.put(4, "David Alaba");
        players.put(5, "Éder Militão");
        players.put(7, "Eden Hazard");
        players.put(9, "Karim Benzema");
        players.put(10, "Luka Modric");
        players.put(11, "Marco Asensio");
        players.put(14, "Casemiro");
        players.put(15, "Federico Valverde");
        players.put(17, "Lucas Vázquez");
        players.put(20, "Vinícius Júnior");

        System.out.print("Enter the jersey number of the player you want to find: "); //promt the user to enter a jersey number
        int jerseyNumber = scanner.nextInt();

        if (players.containsKey(jerseyNumber)) { //check if jersey number is found in the hashmap, and print out if either the jersey is or isnt there
            System.out.println("Player with jersey number " + jerseyNumber + ": " + players.get(jerseyNumber));
        } else {
            System.out.println("No player found with jersey number " + jerseyNumber);
        }
    }
}
