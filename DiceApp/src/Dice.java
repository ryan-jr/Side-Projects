/**
 * Created by rjr on 7/19/2017.
 */
import java.util.*;

public class Dice {

    // Initializing neccessary variables
    private int ctr = 1;
    private int side = 0;


    public Dice() {

        // Accepting user inputs, looping as needed
        // Creating random ints as needed
        System.out.println("How many dice? ");
        Scanner ctrInput = new Scanner(System.in);
        ctr = ctrInput.nextInt();

        System.out.println("How many sides are the die/dice? ");
        Scanner sideInput = new Scanner(System.in);
        side = sideInput.nextInt();

        for(int i = 1; i < ctr + 1; i++) {

            System.out.println("Dice " + i + " is:");
            Random random = new Random();
            int randomNumber = random.nextInt(side - 1) + 1;
            System.out.println(randomNumber);
        }

    }
}