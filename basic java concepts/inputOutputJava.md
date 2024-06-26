# Basic Input and Output in Java
1. scanner class
2. buffered reader


 > Java is a versatile language, that relies on libraries to access various functionalities. To perform tasks like input and output, we include specific libraries at the beginning of our code. One such essential library is java.util, which includes the Scanner class. The Scanner class is a workhorse for handling user input, allowing you to effortlessly read data from the keyboard or other sources.

 > Java offers two input methods, Scanner and BufferedReader, to cater to diverse programming needs. Scanner simplifies console input for common use cases, providing easy-to-use methods for various data types. BufferedReader, on the other hand, offers greater control and efficiency, making it suitable for complex input scenarios and handling large volumes of data, such as reading from files or network streams. 








> [!NOTE]
> to use commonly used utility classes in java like Scanner , ArrayList Hashmap etc , you can import the java.util package and not import java.util.* which imports all the classes and interfaces from java.util.packages  and thus its good to import only the neccessary packages , this helps in keeping our code more efficient and maintainable , as you won't have unnecessary overhead from importing unused libraries .
> consider the impact on compile time, especially in large Java projects.




The generic skeleton of a Java program consists of two main components: the import statements and the main method. After importing the necessary libraries, you declare the main method using public static void main(String[] args) { /* Your code here */ }. This serves as the entry point for your program.


```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Your code here
    }
}
```



## 1) Using Scanner class -to get user input 
One of the fundamental aspects of programming is taking input from the user. In Java, this is achieved with the help of the Scanner class, which allows you to receive input from the user via the terminal or console.
```java
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



## 2) using buffered reader -to get user input 
> BufferedReader is more efficient when dealing with large volumes of input data, such as reading from files or network streams.
> It reads input as a stream of characters and can be particularly useful for handling text-based data where you need to parse lines or process data incrementally.

### Creating a BufferedReader Object
To use BufferedReader, first, we create an object of the InputStreamReader class. This object specifies where the input originates from.
```java
InputStreamReader is = new InputStreamReader(System.in);
```

### Initializing BufferedReader
Now, create a BufferedReader object and pass the InputStreamReader object into it. This BufferedReader will be responsible for reading and processing the input.
```java
InputStreamReader is = new InputStreamReader(System.in);
BufferedReader bf = new BufferedReader(in);
```
Here, the InputStreamReader class is used to convert the raw byte-based input stream (System.in) into a character-based input stream. This is necessary to read text input conveniently.

Now, the BufferedReader is used to buffer the input stream, making it more efficient to read lines of text. It provides methods like readLine() to read complete lines of text, which is very useful for user input.

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class InputOutput {
    public static void main(String[] args) throws IOException {
        System.out.println("Enter a number:"); 
        InputStreamReader in = new InputStreamReader(System.in);
        BufferedReader bf = new BufferedReader(in);

        int num = Integer.parseInt(bf.readLine());
        System.out.println("You entered: " + num);
    }
}
```









## 1) Problem statement 
### Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.

1, if the character is an uppercase alphabet (A - Z).

0, if the character is a lowercase alphabet (a - z).

-1, if the character is not an alphabet.


Example:
Input: The character is 'a'.
Output: 0


## [coding Solution](https://www.codingninjas.com/studio/problems/find-character-case_58513)
```java
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


