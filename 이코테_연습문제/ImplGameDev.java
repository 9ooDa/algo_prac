import java.util.*;

public class ImplGameDev {
    public static void main (String[] args) {
        int n = 4;
        int m = 4;
        int currX = 1;
        int currY = 1;
        int dir = 0;
        int[][] graph = {{1, 1, 1, 1}, {1, 0, 0, 1}, {1, 1, 0, 1}, {1, 1, 1, 1}};
        Map<Integer, int[]> dirDict = new HashMap<>();
        
        int[] north = {0, -1};
        int[] east = {1, 0};
        int[] south = {0, 1};
        int[] west = {-1, 0};
        
        dirDict.put(0, north);
        dirDict.put(1, east);
        dirDict.put(2, south);
        dirDict.put(3, west);

        
        
    }
}
