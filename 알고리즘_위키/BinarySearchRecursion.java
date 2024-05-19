package 알고리즘_위키;

public class BinarySearchRecursion {
    public static int BinarySearch(int[] arr, int target, int start, int end) {
        if(start >  end) return -1;

        int mid = (start + end) / 2;

        if(arr[mid] == target) return mid;
        else if(arr[mid] > target) return BinarySearch(arr, target, start, mid-1);
        else return BinarySearch(arr, target, mid+1, end);
    }

    public static void main(String[] args) {
        int n = 10;
        int target = 7;
        int[] array = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};

        int result = BinarySearch(array, target, 0, n-1);

        if(result == -1) System.out.println("원소가 존재하지 않습니다");
        else System.out.println(result+1);
    }
}
