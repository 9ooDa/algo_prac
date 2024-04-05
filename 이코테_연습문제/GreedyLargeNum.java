// 큰 수의 법칙
import java.util.*;

public class GreedyLargeNum {
    public static void main(String[] args) {
		// int n = 5;
		// int m = 7;
		// int k = 2;
		// // 여기에 int[] numArr 해봤는데 apparently Arrays.sort() doesn't accept array of primitive data type
		// // 그래서 Integer[]로 바꿔줌
		// Integer[] numArr = {3, 4, 3, 4, 3};

        Scanner scan = new Scanner(System.in);
	    
	    // 조건 값들 입력 받기
	    int n = scan.nextInt();
	    int m = scan.nextInt();
	    int k = scan.nextInt();
		Integer[] numArr = new Integer[n];

		for (int i=0; i < n; i++) {
			numArr[i] = scan.nextInt();
		}

		Arrays.sort(numArr, Collections.reverseOrder());

		int ans = 0;
		int count = 0;
		int first = numArr[0];
		int second = numArr[1];

		while (m > 0) {
			if (count < k) {
				ans += first;
				count += 1;
			}
			else {
				ans += second;
				count = 0;
			}

			m -= 1;
		}

		System.out.println(ans);
    }
}