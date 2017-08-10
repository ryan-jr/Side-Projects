/**
 * Created by rjr on 8/6/2017.
 */

import com.sun.org.apache.xpath.internal.SourceTree;

import java.util.*;

public class GroceryList {

    public ArrayList<String> groceryList = new ArrayList<String>();
    int groceryCounter = 0;

    public void addItem(String item) {

        groceryList.add(item);
        System.out.println(item + " added!");
        groceryCounter++;
    }

    public void removeItem(String item) {
        if (groceryList.contains(item)) {

            groceryList.remove(groceryList.indexOf(item));
        } else {

            System.out.println(item + " is not in the list!");
        }

    }


}
