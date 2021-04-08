import java.util.Arrays;
import java.util.Scanner;

public class 백준_14890 {
	static int N, L;
	static int[][] map;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		L = sc.nextInt();
		map = new int[N][N];
		
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				map[i][j] = sc.nextInt();
		
		int ans = 0;
		for(int i=0;i<N;i++) {
			int[] tmp1 = new int[N];
			int[] tmp2 = new int[N];
			for(int j=0;j<N;j++) {
				tmp1[j] = map[i][j];
				tmp2[j] = map[j][i];
			}
			
			if(isRoad(tmp1)) ans++;
			if(isRoad(tmp2)) ans++;

		}
		
		System.out.println(ans);
	}
	
	public static boolean isRoad(int[] road) {
		int j = 0, cnt = 0;
		boolean check = false;
		while(j < N-1) {
			if(road[j] == road[j+1]) {
				if(!check)
					cnt++;
				else
					check = false;
			}
			else if(road[j] + 1 == road[j+1]) {
				if(cnt+1 >= L && !check)
					cnt = 0;
				else
					return false;
			}else if(road[j] == road[j+1] + 1) {
				int c = 1;
				while(c <= L) {
					if(j+c >= N) return false;
					if(road[j] != road[j+c] + 1)
						return false;
					c++;
				}
				j = j + L - 1;
				check = true;
				cnt = 0;
			}else
				return false;
			
			j++;
		}
		
		return true;
	}
}
