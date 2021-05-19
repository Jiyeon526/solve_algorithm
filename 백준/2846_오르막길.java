import java.util.Scanner;

public class 백준_2846_오르막길 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] road = new int[N];
		
		for(int i=0;i<N;i++)
			road[i] = sc.nextInt();
		
		int start = road[0], end = 0, ans = 0;
		for(int i=1;i<N;i++) {
			if(road[i] > road[i-1]) {
				end = road[i];
			}else {
				ans = Math.max(ans, end - start);
				start = road[i];
				end = road[i];
			}
		}
		
		ans = Math.max(ans, end-start);
		System.out.println(ans);
		
	}

}
