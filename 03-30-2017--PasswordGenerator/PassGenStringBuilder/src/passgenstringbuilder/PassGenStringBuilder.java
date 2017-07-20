/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package passgenstringbuilder;

/**
 *
 * @author rjr
 */

import java.util.*;

public class PassGenStringBuilder {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int passwordLen;
        List<Integer> numPassword = new ArrayList<>();
        Random rand = new Random();
        int passwordLenCounter = 0;
        StringBuilder builder = new StringBuilder();
        
        
        
        
        Scanner reader = new Scanner(System.in);
        System.out.println("How long do you want the password to be?");
        System.out.println("Please input a number between 5 and 100");
        passwordLenCounter = reader.nextInt();
        
        // TODO: Put everything in as a set of arrays and then flatten the array?
        
        if (passwordLenCounter < 5 || passwordLenCounter > 100) {
            
            System.out.println("Please input a valid password length");
            
        } else {
            
            while (numPassword.size() < passwordLenCounter) {
                
                numPassword.add(rand.nextInt(10));
            }
            
        }
        
        for (Integer number : numPassword) {
            
            builder.append(number != null ? number.toString() : "");
            
        }
        
        
        System.out.println("Your password is: ");
        System.out.print(builder.toString());
        
                
        
        // To create a password generator given a set of constratins provided by the user
        // Include/Exclude Dictionary
        // Include special characters
        // Include/Exclude upper/lowercase characters
        // Password Length
        
    }
    
}
