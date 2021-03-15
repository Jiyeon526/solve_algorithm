import java.util.Arrays;
import java.util.Scanner;

public class 백준_15657 {
	static int N;
	static int M;
	static int num[];
	
	public static void comb(int cnt, int comb_num[], int last) {
		if(cnt == M) {
			for(int i=0;i<cnt;i++)
				System.out.print(comb_num[i] + " ");
			System.out.println();
			return;
		}
		
		for(int i=0;i<N;i++) {
			// 마지막으로 들어간 수 보다 크거나 같은 수만
			if(last <= num[i]) {
				comb_num[cnt] = num[i];
				comb(cnt+1, comb_num, num[i]);
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		num = new int[N];
		
		for(int i=0;i<N;i++)
			num[i] = sc.nextInt();
		
		Arrays.sort(num); //정렬
		int num_d[] = new int[M]; // 조합으로 만든 숫자 저장
		comb(0, num_d, num[0]);
	}

}
