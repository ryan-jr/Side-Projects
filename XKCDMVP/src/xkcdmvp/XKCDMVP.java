/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package xkcdmvp;

/**
 *
 * @author rjr
 */

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;
import java.lang.Math.*;


public class XKCDMVP {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner pwLength = new Scanner(System.in);
        
        System.out.println("Please enter how long you want the password to be: ");
        int length = pwLength.nextInt();
        int[] passwordArray = new int[length];
        double passwordStrength = Math.log(Math.pow(94, length));
        
        for (int i = 0; i < length; i++) {
            
            int randomNum = ThreadLocalRandom.current().nextInt(33, 125 + 1);
            passwordArray[i] = randomNum;
            
        }
        
        for (int num : passwordArray) {
            
            System.out.print((char) num);
        }
        System.out.println(" ");
        System.out.println(length);
        System.out.println();
        System.out.println(passwordStrength);
        
        
        
    }
    
}
