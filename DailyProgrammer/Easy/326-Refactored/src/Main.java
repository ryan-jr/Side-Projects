import java.util.Scanner;

/**
 * Created by rjr on 8/9/2017.
 */

// REFACTORED VERSION (NOW WITH METHODS!!!)
public class Main {


    /**
     *
     *
     * A prime number is any integer greater than 1 which can only be evenly divided by 1 or itself. For this challenge,
     * you will output two numbers: the nearest prime below the input, and the nearest prime above it.
     *
     * The format of the output will be:
     * p1 < n < p2
     * where p1 is the smaller prime, p2 is the larger prime and n is the input.
     * If n already is a prime, the output will be:
     * n is prime.
     *
     * The following is an initial brute force solution using for loops and if statements.
     */
    public static void main(String[] args) {


        int x = 525;
        int y = 99;
        int z = 3;

        int ctr = 0;
        int ctr1 = 0;
        int ctr2 = 0;

     public int primeCheck(int num) {

         int ctr = 0;
        for(int i = 2; i < num; i++) {

            if(num % i == 0) {

                ctr++;
            }
        }

        return ctr;

    }

        // Looping through and checking if the number is prime


        // Looping through if the number is not prime, and finding the next lowest prime
        if(ctr > 1) {

            for(int i = num - 1; i <= num; i--) {

                if((i % 2 != 0) && (i % 3 != 0)) {

                    System.out.println(i + " is less than " + num + " and is prime.");
                    break;
                }
            }

            // Looping through and finding the next greatest prime.
            for(int i = num + 1; i >= num; i++) {

                if((i % 2 != 0) && (i % 3 != 0) && (i % 5 != 0)) {

                    System.out.println(i + " is greater than " + num + " and is prime.");
                    break;
                }
            }


        } else {

            System.out.println(num + " is prime.");
            System.out.println(ctr);
        }
    }
}
