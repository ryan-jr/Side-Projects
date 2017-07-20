// Java dice roller

import java.util.*;

public class Main{

    public static void main(String[] args) {

        // Initializing input variable
        int userInput = 0;

        // Accepting user input creating new Dice class
        while(userInput != 2) {


            System.out.println("Please make your selection:");
            System.out.println("1.  Roll dice");
            System.out.println("2.  Quit");

            Scanner in = new Scanner(System.in);
            userInput = in.nextInt();

            if(userInput == 1) {

                Dice d = new Dice();

            }

        }

        System.out.println(userInput);
    }
}
