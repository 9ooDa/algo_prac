import java.util.*;

public class GreedyNumberCardGame {
    public static void main(String[] args) {
        int n = 2;
        int m = 4;
        int[][] cards = {{7, 3, 1, 8},{3, 3, 3, 4}};
        int result = 0;
        
        for (int i=0; i < n; i++) {
            int row_min = Arrays.stream(cards[i]).min().orElse(0);
            result = Math.max(result, row_min);
        }

        System.out.println(result);
    }
}
