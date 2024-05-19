import java.util.*;
import java.awt.Point;

public class BFSMaze {
    static int n = 5;
    static int m = 6;
    static int[][] graph = {{1, 0, 1, 0, 1, 0}, {1, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 1}, {1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1}};
    static int count = 0;

    public static void main (String[] args) {
        System.out.println(bfs(0, 0));
    }

    public static int bfs (int x, int y) {
        Queue<Point> q = new LinkedList<>();
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        q.offer(new Point(x, y));

        while (!q.isEmpty()) {
            Point p = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = (p.x + dx[i]);
                int ny = (p.y + dy[i]);

                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

                if (graph[nx][ny] == 0) continue;

                if (graph[nx][ny] == 1) {
                    graph[nx][ny] = graph[p.x][p.y] + 1;
                    q.offer(new Point(nx, ny));
                }
            }
        }

        return graph[n-1][m-1];
    }
}
