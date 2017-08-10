import java.util.Scanner;

/**
 * Created by rjr on 8/9/2017.
 */
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
     *
     */
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        System.out.print("Please input the number to analyze");
        int num = in.nextInt();
        System.out.println("Checking...");

        int ctr = 0;
        int ctr1 = 0;
        int ctr2 = 0;

        for(int i = 2; i < num; i++) {

            if(num % i == 0) {

                ctr++;
            }
        }
        System.out.println(ctr);

        if(ctr > 1) {

            for(int i = num - 1; i <= num; i--) {

                if((i % 2 != 0) && (i % 3 != 0)) {

                    System.out.println(i + " is less than " + num + " and is prime.");
                    break;
                }
            }

            for(int i = num + 1; i >= num; i++) {

                if((i % 2 != 0) && (i % 3 != 0)) {

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
