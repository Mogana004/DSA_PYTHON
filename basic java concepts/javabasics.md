Problem statement
Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.

1, if the character is an uppercase alphabet (A - Z).
0, if the character is a lowercase alphabet (a - z).
-1, if the character is not an alphabet.


Example:
Input: The character is 'a'.
Output: 0

```
import java.util.*;
public class Solution {
    
    public static void main(String[] args) {
        
        Scanner scannerclass = new Scanner(System.in);
        
        char inputChar = scannerclass.next().charAt(0);
        scannerclass.close();
         if (inputChar >= 'A' && inputChar <= 'Z') {
            System.out.println("1");
        }
        else if (inputChar >= 'a' && inputChar <= 'z') {
            System.out.println("0");
        }
        else{
            System.out.println("-1");
        }
       

    }
}
```![Screenshot (621)](https://github.com/Mogana004/DSA_JAVA/assets/92911280/46410360-5634-4486-968d-7601f341050d)

