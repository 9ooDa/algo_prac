import java.util.*;

public class BSTteokbokki {
    public static void main(String[] args) {
        int n = 4;
        int m = 6;
        int[] array = {19, 15, 10, 17};
        Arrays.sort(array);

        System.out.println(BinarySearch(array, m, 0, array[n-1]));
    }

    public static int BinarySearch(int[] arr, int target, int start, int end) {
        int result = 0;
        while(start <= end) {
            int total = 0;
            int mid = (start + end) / 2;

            for(int x : arr) {
                if(x > mid) {
                    total += x - mid;
                }
            }

            if(total < target) end = mid - 1;
            else {
                result = mid;
                start = mid + 1;
            }
        }
        return result;
    }
}
