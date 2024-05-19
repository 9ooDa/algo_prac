public class DFSJuice {

    static int n = 4;
    static int m = 5;
    static int[][] graph = {{0, 0, 1, 1, 0}, {0, 0, 0, 1, 1}, {1, 1, 1, 1, 1}, {0, 0, 0, 0, 0}};
    public static void main (String[] args) {
        int result = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (dfs(i, j) == true) result++;
            }
        }

        System.out.println(result);
    }

    public static boolean dfs (int x, int y) {
        if (x < 0 || x >= n || y < 0 || y >= m) return false;

        if (graph[x][y] == 0) {
            graph[x][y] = 1;
            dfs(x-1, y);
            dfs(x+1, y);
            dfs(x, y-1);
            dfs(x, y+1);
            return true;
        }

        return false;
    }
}
