import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class swea_탈주범검거 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int t=1;t<=TC;t++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int R = sc.nextInt();
			int C = sc.nextInt();
			int L = sc.nextInt();
			
			int[][] map = new int[N][M];
			boolean[][] visit = new boolean[N][M];
			
			for(int i=0;i<N;i++)
				for(int j=0;j<M;j++)
					map[i][j] = sc.nextInt();
			
			int[] dx = {0, 1, 0, -1}, dy = {1, 0, -1, 0}; // 우하좌상
			boolean[][] pipe = new boolean[8][4];
			
			for(int i=0;i<4;i++) {
				pipe[1][i] = true;
				if(i == 0) {
					pipe[3][i] = true;
					pipe[4][i] = true;
					pipe[5][i] = true;
				}else if(i == 1) {
					pipe[2][i] = true;
					pipe[5][i] = true;
					pipe[6][i] = true;
				}else if(i == 2) {
					pipe[3][i] = true;
					pipe[6][i] = true;
					pipe[7][i] = true;
				}else {
					pipe[2][i] = true;
					pipe[4][i] = true;
					pipe[7][i] = true;
				}
			}
			
			visit[R][C] = true;
			int time = 1;
			int cnt = 1;
			Queue<int[]> q = new LinkedList<>();
			q.offer(new int[]{R, C});
			
			while(!q.isEmpty() && time <= L) {
				int size = q.size();
				time++;
				
				for(int s=0;s<size;s++) {
					int[] now = q.poll();
//					System.out.println("now = " + Arrays.toString(now));
					
					for(int d=0;d<4;d++) {
						if(pipe[map[now[0]][now[1]]][d]) {
							int nx = now[0] + dx[d];
							int ny = now[1] + dy[d];
//							System.out.println("move = " + nx + " " + ny);
							
							if(nx>=0 && nx<N && ny>=0 && ny<M && !visit[nx][ny] && map[nx][ny] != 0) {
								if(pipe[map[nx][ny]][(d+2)%4]) {
									visit[nx][ny] = true;
									cnt++;
									q.offer(new int[] {nx, ny});
								}
							}
						}
					}
				}
//				System.out.println();
			}
			cnt -= q.size();
			System.out.println("#" + t + " " + cnt);
		}

	}

}
