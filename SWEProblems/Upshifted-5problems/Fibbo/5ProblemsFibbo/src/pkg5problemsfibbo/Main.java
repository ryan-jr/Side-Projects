/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkg5problemsfibbo;

/**
 *
 * @author rjr
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int fib1 = 0;
        int fib2 = 1;
        
        for (int i = 0; i < 10; i++) {
            
            int fibbo = fib1 + fib2;
            fib1 = fib2;
            fib2 = fibbo;
            
            System.out.println(fibbo);
            
        }
    }
    
}
