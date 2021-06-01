import java.util.Scanner;

public class swea_지뢰 {

	static int N;
	static boolean[][] visit;
	static int[][] num;
	static int[] dx = {-1, 0, 1, 0, -1, -1, 1, 1};
	static int[] dy = {0, 1, 0, -1, 1, -1, -1, 1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int t=1;t<=TC;t++) {
			N = sc.nextInt();
			char[][] map = new char[N][N];
			visit = new boolean[N][N];
			num = new int[N][N];
			
			for(int i=0;i<N;i++) {
				String s = sc.next();
				for(int j=0;j<N;j++)
					map[i][j] = s.charAt(j);
			}
			
			for(int i=0;i<N;i++)
				for(int j=0;j<N;j++) {
					if(map[i][j] == '*') {
						num[i][j] = -1;
						visit[i][j] = true;
						continue;
					}
					
					int cnt = 0;
					for(int d=0;d<8;d++) {
						int nx = i + dx[d];
						int ny = j + dy[d];
						
						if(nx>=0 && nx<N && ny>=0 && ny<N)
							if(map[nx][ny] == '*') cnt++;
						
					}
					
					num[i][j] = cnt;
				}
			
			int ans = 0;
			for(int i=0;i<N;i++)
				for(int j=0;j<N;j++)
					if(!visit[i][j] && num[i][j] == 0) {
						ans++;
						visit[i][j] = true;
						dfs(i, j);
					}
			
			for(int i=0;i<N;i++)
				for(int j=0;j<N;j++)
					if(!visit[i][j]) ans++;
			
			System.out.println("#" + t + " " + ans);
		}
		
		
		
	}

	private static void dfs(int i, int j) {
		for(int d=0;d<8;d++) {
			int nx = i + dx[d];
			int ny = j + dy[d];
			
			if(nx>=0 && nx<N && ny>=0 && ny<N) {
				if(!visit[nx][ny] && num[nx][ny] > 0)
					visit[nx][ny] = true;
				else if(!visit[nx][ny] && num[nx][ny] == 0) {
					visit[nx][ny] = true;
					dfs(nx, ny);
				}
			}
		}
		
	}
	
	

}
