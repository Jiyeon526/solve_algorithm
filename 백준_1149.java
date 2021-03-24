import java.util.Scanner;

public class 백준_1149 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int home[][] = new int[N][3];
		int sum[][] = new int[N][3];
		
		for(int i=0;i<N;i++) {
			home[i][0] = sc.nextInt();
			home[i][1] = sc.nextInt();
			home[i][2] = sc.nextInt();
		}
	
		sum[0][0] = home[0][0];
		sum[0][1] = home[0][1];
		sum[0][2] = home[0][2];
		
		for(int i=1;i<N;i++) {
			sum[i][0] = Math.min(sum[i-1][1], sum[i-1][2]) + home[i][0];
			sum[i][1] = Math.min(sum[i-1][0], sum[i-1][2]) + home[i][1];
			sum[i][2] = Math.min(sum[i-1][0], sum[i-1][1]) + home[i][2];
		}
		
		int cost = sum[N-1][0];
		for(int i=1;i<3;i++)
			cost = Math.min(cost,  sum[N-1][i]);
		
		System.out.println(cost);
	}

}
