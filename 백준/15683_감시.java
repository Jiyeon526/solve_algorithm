import java.util.Scanner;

public class 백준_15683_감시 {

	static int N, M, cctvCnt, ans;
	static Point[] cctv;
	static int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1}; //상하좌우
	static String[][] cctvDir = { // cctv방향 정보
		{},
		{"0","1","2","3"},
		{"01", "23"},
		{"03","02","13","12"},
		{"032","013","312","120"},
		{"0123"}
	};
	
	static class Point {
		int x, y;

		public Point(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}

		@Override
		public String toString() {
			return "Point [x=" + x + ", y=" + y + "]";
		}
		
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		cctv = new Point[8]; // cctv있는 좌표
		cctvCnt = 0;
		int[][] map = new int[N][M];

		// 좌표 입력
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++) {
				map[i][j] = sc.nextInt();
				if(map[i][j] > 0 && map[i][j] != 6) {
					cctv[cctvCnt] = new Point(i, j);
					cctvCnt++;
				}	
			}
		
		ans = Integer.MAX_VALUE;
		find(map, 0);
		System.out.println(ans);
	}
	
	public static void find(int[][] map, int idx) {
		if(idx == cctvCnt) {
			ans = Math.min(ans, total(map));
			return;
		}
		
		String[] nowDir = cctvDir[map[cctv[idx].x][cctv[idx].y]]; // cctv 방향들
		for(int i=0;i<nowDir.length;i++) {
			int[][] newMap = copy(map);
			
			for(int j=0;j<nowDir[i].length();j++) {
				int nowX = cctv[idx].x;
				int nowY = cctv[idx].y;
				int dir = nowDir[i].charAt(j) - '0'; // 현재 가야되는 방향
				
				while(true) {
					nowX += dx[dir];
					nowY += dy[dir];
					
					if(nowX<0 || nowX>=N || nowY<0 || nowY>=M) break;
					if(newMap[nowX][nowY] == 6) break;
					if(newMap[nowX][nowY] > 0) continue;
					newMap[nowX][nowY] = 7;
				}
			}
			
			find(newMap, idx+1);
		}
	}
	
	private static int[][] copy(int[][] map) { // map 복사
		int[][] newMap = new int[N][M];
		
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				newMap[i][j] = map[i][j];
		
		return newMap;
	}

	public static int total(int[][] map) { // 0개수세기
		int result = 0;
		
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				if(map[i][j] == 0)
					result++;
		
		return result;
	}

}
