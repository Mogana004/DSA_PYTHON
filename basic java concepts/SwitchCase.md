![image](https://github.com/Mogana004/DSA_JAVA/assets/92911280/8f2f5ac4-6021-4f44-b687-4880fd86d651)
```java
public class Solution {
    public static double areaSwitchCase(int ch, double []a) {
        double area = 0.0;

        // Using switch-case to figure out whose area we want to find

        switch (ch) {

            case 1: // Circle
                area = Math.PI * a[0] * a[0];
                break;

            case 2: // Rectangle
                area = a[0] * a[1];

        }

        // Returning the calculated area
        return area;
    }
}
```    
