import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class 백준_15666 {
	static int N;
	static int M;
	static ArrayList<Integer> num;

	
	public static void comb(int cnt, int comb_num[], int last) {
		if(cnt == M) {
			for(int i=0;i<cnt;i++) {
				System.out.print(comb_num[i] + " ");
			}
			System.out.println();
			return;			
		}
		
		for(int i=0;i<num.size();i++) {
			if(last <= num.get(i)) {
				comb_num[cnt] = num.get(i);
				comb(cnt+1, comb_num, num.get(i));
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		num = new ArrayList<>();
	
		for(int i=0;i<N;i++) {
			int n = sc.nextInt();
			if(!num.contains(n))
				num.add(n);
		}
		
		num.sort(null);
		int num_d[] = new int[M];
		comb(0, num_d, num.get(0));
	}

}
