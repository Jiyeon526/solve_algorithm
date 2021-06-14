import java.util.Scanner;

public class 백준_11265_끝나지않는파티 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[][] map = new int[N][N];
		
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				map[i][j] = sc.nextInt();

		for (int k = 0; k < N; k++) {
	        for (int i = 0; i < N; i++) {
	            for (int j = 0; j < N; j++) {
	                if (map[i][j] > map[i][k] + map[k][j]) {
	                    map[i][j] = map[i][k] + map[k][j];
	                }
	            }
	        }
	    }
		
		for(int i=0;i<M;i++) {
			int A = sc.nextInt();
			int B = sc.nextInt();
			int C = sc.nextInt();
			
			if(map[A-1][B-1] <= C)
				System.out.println("Enjoy other party");
			else
				System.out.println("Stay here");
		}
	}
}
