import java.util.*;

public class ImplKnights {
    public static void main (String[] args) {
        String curr = "a1";
        Map<Character, Integer> dict = new HashMap<>() {{
            put('a', 1);
            put('b', 2);
            put('c', 3);
            put('d', 4);
            put('e', 5);
            put('f', 6);
            put('g', 7);
            put('h', 8);
        }};
        int x = dict.get(curr.charAt(0));
        int y = curr.charAt(1) - '0';

        int count = 0;
        int[][] stepsArr = {{-2, -1}, {-2, 1}, {2, -1}, {2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}};

        for (int[] step : stepsArr) {
            int dx = step[0];
            int dy = step[1];

            if (x+dx < 1 || x+dx > 8 || y+dy < 1 || y+dy > 8) {
                continue;
            }
            else {
                count += 1;
            }
        }
        System.out.println(count);
    }    
}
