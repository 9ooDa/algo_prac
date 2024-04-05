import java.util.*;

public class GreedyUntilOne {
    public static void main(String[] args) {
        int n = 17;
        int k = 4;
        int count = 0;

        while (true) {
            if (n == 1) {
                break;
            }
            if (n % k == 0) {
                n /= k;
            }
            else {
                n -= 1;
            }
            count += 1;
        }

        System.out.println(count);
    }
}
