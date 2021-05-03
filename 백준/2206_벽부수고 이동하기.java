import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 백준_2206_벽부수고이동하기 {

	static int N, M;
	static int[][] map;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		map = new int[N][M];
		
		for(int i=0;i<N;i++) {
			String s = sc.next();
			for(int j=0;j<M;j++)
				map[i][j] = s.charAt(j) - '0';
		}
		
		System.out.println(bfs());
	}

	public static int bfs() {
		int[] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};
		boolean[][][] visit = new boolean[N][M][2]; // x, y, 벽부쉈는지 체크
		Queue<int[]> q = new LinkedList<>();
		
		q.add(new int[] {0, 0, 0}); // 시작점 넣어주기(x, y, 벽부쉈는지 0은 안부숨 1은 부숨)
		visit[0][0][0] = true;
		int cnt = 0; // 최단 거리
		
		while(!q.isEmpty()) {
			int size = q.size();
			cnt++;
		
			for(int s=0;s<size;s++) {
				int[] now = q.poll();
				
				if(now[0] == N-1 && now[1] == M-1)
					return cnt;
				
				for(int d=0;d<4;d++) {
					int nx = now[0] + dx[d];
					int ny = now[1] + dy[d];
					
					if(nx<0 || nx>=N || ny<0 || ny>=M) continue;
					if(now[2] == 1 && map[nx][ny] == 1) continue;
					
					// 벽 부숨, 다음 칸이 이동할 수 있는 칸, 방문 안했으면 넣어주기
					if(now[2] == 1 && map[nx][ny] == 0 && !visit[nx][ny][1]) {
						q.add(new int[] {nx, ny, 1});
						visit[nx][ny][1] = true;
					}
					
					if(now[2] == 0 && !visit[nx][ny][0]) { // 벽 안부숨
						if(map[nx][ny] == 0)  // 갈려는 곳이 이동할 수 있는 칸이면 그냥 넣어주기
							q.add(new int[] {nx, ny, 0});
						else// 벽이라면 벽을 부수고 넣어주기
							q.add(new int[] {nx, ny, 1});
						visit[nx][ny][0] = true;
					}
					
				}
			}
		}
		
		return -1;
	}
}
