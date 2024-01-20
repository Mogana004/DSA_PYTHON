### Basic Input and Output in Java
1. scanner class
2. buffered reader


 > Java is a versatile language, that relies on libraries to access various functionalities. To perform tasks like input and output, we include specific libraries at the beginning of our code. One such essential library is java.util, which includes the Scanner class. The Scanner class is a workhorse for handling user input, allowing you to effortlessly read data from the keyboard or other sources.

 > Java offers two input methods, Scanner and BufferedReader, to cater to diverse programming needs. Scanner simplifies console input for common use cases, providing easy-to-use methods for various data types. BufferedReader, on the other hand, offers greater control and efficiency, making it suitable for complex input scenarios and handling large volumes of data, such as reading from files or network streams. 








> [!NOTE]
> to use commonly used utility classes in java like Scanner , ArrayList Hashmap etc , you can import the java.util package and not import java.util.* which imports all the classes and interfaces from java.util.packages  and thus its good to import only the neccessary packages , this helps in keeping our code more efficient and maintainable , as you won't have unnecessary overhead from importing unused libraries .
> consider the impact on compile time, especially in large Java projects.




The generic skeleton of a Java program consists of two main components: the import statements and the main method. After importing the necessary libraries, you declare the main method using public static void main(String[] args) { /* Your code here */ }. This serves as the entry point for your program.


```
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Your code here
    }
}
```



## Taking User Input Using Scanner
One of the fundamental aspects of programming is taking input from the user. In Java, this is achieved with the help of the Scanner class, which allows you to receive input from the user via the terminal or console.
```
import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        int x;
        Scanner scanner = new Scanner(System.in);
        x = scanner.nextInt();
        System.out.println("Value of x: " + x);
        scanner.close();
    }
}
```
the Scanner class captures that value, stores it in the variable x, and then displays it using System.out.println.









 Problem statement
Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.

1, if the character is an uppercase alphabet (A - Z).

0, if the character is a lowercase alphabet (a - z).

-1, if the character is not an alphabet.


Example:
Input: The character is 'a'.
Output: 0


## coding Solution
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
```
![Screenshot (621)](https://github.com/Mogana004/DSA_JAVA/assets/92911280/46410360-5634-4486-968d-7601f341050d)


