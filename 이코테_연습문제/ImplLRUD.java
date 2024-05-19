import java.util.*;

public class ImplLRUD {
    public static void main (String[] args) {
        int n = 5;
        String[] directions = {"R", "R", "R", "U", "D", "D"};

        int x = 1;
        int y = 1;

        for (String dir : directions) {
            int dx = 0;
            int dy = 0;

            switch (dir) {
                case "L": 
                    dy = -1;
                    break;
                case "R": 
                    dy = 1;
                    break;
                case "U":
                    dx = -1;
                    break;
                case "D":
                    dx = 1;
                    break;
            }

            if (x+dx <= 0 || x+dx > n || y+dy <= 0 || y+dy >= n) {
                continue;
            }
            else {
                x += dx;
                y += dy;
            }
        }
        System.out.println(x + " " + y);

    }
}
