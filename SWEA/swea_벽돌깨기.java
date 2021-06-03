import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class swea_벽돌깨기 {

	private static int N, W, H, min;
	private static int[] dr = {-1, 1, 0, 0};
	private static int[] dc = {0, 0, -1, 1};
	
	static class Point {
		int r, c, cnt;

		public Point(int r, int c, int cnt) {
			super();
			this.r = r;
			this.c = c;
			this.cnt = cnt;
		}

	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(in.readLine());
		for(int t=1;t<=TC;t++) {
			StringTokenizer st = new StringTokenizer(in.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			H = Integer.parseInt(st.nextToken());
			
			int[][] map = new int[H][W];
			
			for(int i=0;i<H;i++) {
				st = new StringTokenizer(in.readLine(), " ");
				for(int j=0;j<W;j++)
					map[i][j] = Integer.parseInt(st.nextToken());
			}
			
			min = Integer.MAX_VALUE; // 남은 벽돌 갯수
			go(0, map); // 구슬 떨구기
			System.out.println("#" + t + " " + min);
		}
	}

	// 중복 순열로 구슬 떨구기
	// boolean true면 모두 깨진 상황
	private static boolean go(int cnt, int[][] map) {
		int result = getRemain(map);
		if(result == 0) { // 께뜨릴 벽돌 없음
			min = 0;
			return true;
		}
		
		if(cnt == N) {
			min = Math.min(min, result);
			return false;
		}
	
		int[][] newMap = new int[H][W];
		// 매 열마다 구슬을 떨구는 시도
		for(int c=0;c<W;c++) {
			// 해당 열에 구슬을 떨궈 맞는 벽돌 찾기
			int r = 0;
			while(r < H && map[r][c] == 0) ++r;
			if(r == H) // 맞는 벽돌 없음(모두 빈칸)
				continue; // 다음 열로 구슬 떨어뜨리기
			else {
				// 기존 cnt-1 구슬까지의 상태로 초기화
				copy(map, newMap);
				// 벽돌 깨기
				boom(newMap, r, c);
				// 벽돌 내리기
				down(newMap);
				if(go(cnt+1, newMap)) return true;
			}
		}
		
		return false;
	}

	private static int getRemain(int[][] map) {
		int count = 0;
		
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				if(map[i][j] > 0) ++count;
		
		return count;
	}

	// down 다른 방법: List에 남아있는 벽돌 넣기
	private static ArrayList<Integer> list = new ArrayList<Integer>();
	
	private static void down(int[][] map) {
		
		for(int c=0;c<W;c++) {
			int r;
			for(r = H-1;r>=0;r--) {
				if(map[r][c]>0) {
					list.add(map[r][c]); // 벽돌이면
					map[r][c] = 0;
				}
			}// 벽돌 리스트에 넣기
			r = H;
			for(int b: list) {
				map[--r][c] = b;
			}
			list.clear();
		}
		
	}

	private static void boom(int[][] map, int r, int c) {
		Queue<Point> q = new LinkedList<>();
		
		if(map[r][c] > 1)
			q.offer(new Point(r, c, map[r][c]));
		
		map[r][c] = 0; // 제거 처리
	
		while(!q.isEmpty()) {
			Point p = q.poll();
			
			for(int d=0;d<4;d++) {
				int nr = p.r;
				int nc = p.c;
				
				for(int k=1;k<p.cnt;k++) {
					nr += dr[d];
					nc += dc[d];
					
					if(nr>=0 && nr<H && nc>=0 && nc<W && map[nr][nc] != 0) {
						if(map[nr][nc] > 1)
							q.offer(new Point(nr, nc, map[nr][nc]));
						map[nr][nc] = 0;
					}
				}
			}
		}
	}

	private static void copy(int[][] map, int[][] newMap) {
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				newMap[i][j] = map[i][j]; // 매개변수로 들어와서 굳이 return안해도됨
	}
	
	
}
