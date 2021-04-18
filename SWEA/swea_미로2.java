package 보충;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class swea_미로2 {
	
	static class location {
		int x, y;

		public location(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
		
	}
	
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t=0;t<10;t++) {
			int TC = sc.nextInt();
			int[][] map = new int[100][100];
			int startX = 0, startY = 0, endX = 0, endY = 0;
			
			for(int i=0;i<100;i++) {
				String s = sc.next();
				for(int j=0;j<100;j++) {
					map[i][j] = s.charAt(j) - '0';
					if(map[i][j] == 2) {
						startX = i;
						startY = j;
					}else if(map[i][j] == 3) {
						endX = i;
						endY = j;
					}
				}
			}

			Queue<location> q = new LinkedList<>();
			boolean[][] visit = new boolean[100][100];
			q.add(new location(startX, startY));
			visit[startX][startY] = true;
			int ans = 0;
			
			while(!q.isEmpty()) {
				location L = q.poll();
				
				if(L.x == endX && L.y == endY) {
					ans = 1;
					break;
				}
					
				
				for(int i=0;i<4;i++) {
					int nx = L.x + dx[i];
					int ny = L.y + dy[i];
					
					if(0 <= nx && nx < 100 && 0 <= ny && ny < 100) 
						if(!visit[nx][ny] && map[nx][ny] != 1) {
							visit[nx][ny] = true;
							q.add(new location(nx, ny));
						}
					
				}
			}
			
			System.out.println("#" + TC + " " + ans);
		}

	}

}
