/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication2;

/**
 *
 * @author rjr
 */

import java.util.*;

public class JavaApplication2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int passwordLen;
        List<Integer> numPassword = new ArrayList<>();
        Random rand = new Random();
        int passwordLenCounter = 0;
        
        
        Scanner reader = new Scanner(System.in);
        System.out.println("How long do you want the password to be?");
        System.out.println("Please input a number between 5 and 100");
        passwordLenCounter = reader.nextInt();
        
        // TODO: Put everything in as a set of arrays and then flatten the array?
        
        if (passwordLenCounter < 5 || passwordLenCounter > 100) {
            
            System.out.println("Please input a valid password length");
            
        } else {
            
            System.out.println(numPassword.size());
            while (numPassword.size() < passwordLenCounter) {
                
                numPassword.add(rand.nextInt(10));
                System.out.println(numPassword.size());
            }
            
        }
        
        System.out.println("Your password is: ");
        System.out.print(numPassword);
        
                
        
        // To create a password generator given a set of constratins provided by the user
        // Include/Exclude Dictionary
        // Include special characters
        // Include/Exclude upper/lowercase characters
        // Password Length
        
    }
    
}
