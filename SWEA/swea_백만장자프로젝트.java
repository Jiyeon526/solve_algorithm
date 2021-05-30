import java.util.Scanner;

public class swea_백만장자프로젝트 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int tc=1;tc<TC+1;tc++) {
			int N = sc.nextInt();
			int num[] = new int[N+1];
			
			long total = 0;
			for(int i=1;i<N+1;i++) {
				num[i] = sc.nextInt();
				total += num[i];
			}
			
			long max = 0;
			long ans = 0;
			for(int i=1;i<N+1;i++) {
				total += num[i];
				long sum = num[i] * (i-1) - total;
				if(max <= sum) {
					ans += sum;
					max = 0;
				}
			}
			
			System.out.println("#" + tc + " " + ans);
		}
			
		
	}

}
