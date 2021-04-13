import java.util.Arrays;
import java.util.Scanner;

public class swea_활주로건설 {

	static int N, X;
	static int[][] map;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		for(int t=1;t<=TC;t++) {
			N = sc.nextInt();
			X = sc.nextInt();
			map = new int[N][N];
			
			for(int i=0;i<N;i++)
				for(int j=0;j<N;j++)
					map[i][j] = sc.nextInt();
			
			int cnt = 0;
			for(int i=0;i<N;i++) {
				int[] tmp1 = new int[N];
				int[] tmp2 = new int[N];
				
				for(int j=0;j<N;j++)
					tmp1[j] = map[i][j];
				
				for(int j=0;j<N;j++)
					tmp2[j] = map[j][i];
				
				if(isRoad(tmp1)) cnt++;
				if(isRoad(tmp2)) cnt++;

			}		
			System.out.println("#" + t + " " + cnt);
		}
	}

	private static boolean isRoad(int[] tmp) {
		int idx = 1;
		int check = 0;
		boolean[] visit = new boolean[N];
		
		while(idx < N) {
			if(tmp[idx-1] == tmp[idx]) {
				if(!visit[idx-1]) {
					check++;
					visit[idx-1] = true;
				}
			}else if(tmp[idx-1] + 1 == tmp[idx]) {
				if(check >= X-1) {
					check = 0;
					visit[idx-1] = true;
				}else
					return false;
			}else if(tmp[idx-1] == tmp[idx] + 1) {
				int x = 0;
				for(int i = idx;i < idx+X && i < N;i++) {
					if(tmp[idx] != tmp[i])
						return false;
					x++;
					visit[i] = true;
				}
				if(x != X)
					return false;
				idx = idx + X - 1;
				check = 0;
			}else
				return false;
			idx++;
		}
		
		return true;
	}

}
