//처음에 순열로 뽑아 버림
package 보충;

import java.util.Arrays;
import java.util.Scanner;

public class swea_장훈이선반 {
	static int N, B, small_d;
	static int[] H;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		for(int t=1;t<tc+1;t++) {
			N = sc.nextInt();
			B = sc.nextInt();
			H = new int[N];
			
			for(int i=0;i<N;i++)
				H[i] = sc.nextInt();
			
			small_d = Integer.MAX_VALUE;
			for(int i=1;i<N+1;i++) {
				find(i, 0, 0, 0);
				if(small_d == 0)
					break;
			}
			
			System.out.println("#" + t + " " + small_d);
		}

	}
	
	public static void find(int I, int cnt, int H_sum, int idx) {
		if(I == cnt) {
			int x = H_sum - B;
			if(x == 0)
				small_d = 0;
			if(x > 0 && x < small_d)
				small_d = x;
			return;
		}else if(idx >= N) {
			return;
		}

		find(I, cnt, H_sum, idx+1);
		find(I, cnt+1, H_sum+H[idx], idx+1);
	}

}


/*for(int i=0;i<N;i++){
	if(!visit[i])
		visit[i] = true;
		find(I, cnt+1, H_sum+H[i]);
		visit[i] = false;
}

조합으로짤때는 입력값의 ? 절반값이면? 노노노..
3월 18일 교수님 풀이가 더 좋은듯 나는 뭔가 필요 없는것까지 한것같음
*/