public class BSFindParts {
    public static void main(String[] args) {
        int n = 5;
        int[] inStock = {8, 3, 7, 9, 2};
        int m = 3;
        int[] inNeed = {5, 7, 9};

        for(int target : inNeed) {
            System.out.println(BinarySearch(inStock, target, 0, n-1));
        }
    }

    public static String BinarySearch(int[] arr, int target, int start, int end) {
        if(start > end) return "no";

        int mid = (start + end) / 2;

        if(arr[mid] == target) return "yes";
        else if(arr[mid] > target) return BinarySearch(arr, target, start, mid-1);
        else return BinarySearch(arr, target, mid+1, end);
    }
}
