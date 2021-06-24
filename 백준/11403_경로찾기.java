import java.util.Scanner;

public class 백준_11403_경로찾기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] map = new int[N][N];
		
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++) 
				map[i][j] = sc.nextInt();

		for(int k=0;k<N;k++)
			for(int i=0;i<N;i++)
				for(int j=0;j<N;j++) {
					if(map[i][k] == 1 && map[k][j] == 1) {
						map[i][j] = 1;
					}
				}
		
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++)
				System.out.print(map[i][j] + " ");
			System.out.println();
		}
		
	}
}
