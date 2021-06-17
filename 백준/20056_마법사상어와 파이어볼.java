import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 백준_20056_마법사상어와_파이어볼 {
	
	static int N, M, K;
	static List<Fireball>[][] map;
	static List<Fireball> list = new ArrayList<>();
	static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
	static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
	
	static class Fireball{
		int x, y, m, s, d;

		public Fireball(int x, int y, int m, int s, int d) {
			this.x = x; this.y = y; this.m = m; this.s = s; this.d = d;
		}

		@Override
		public String toString() {
			return "Fireball [x=" + x + ", y=" + y + ", m=" + m + ", s=" + s + ", d=" + d + "]";
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken()); 
		M = Integer.parseInt(st.nextToken()); 
		K = Integer.parseInt(st.nextToken());
		map = new List[N][N];
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) map[i][j] = new ArrayList<>();
		}
		
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			// 위치, 질량, 속도, 방향
			list.add(new Fireball(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		
		System.out.println(move());
	}
	
	public static int move() {
		int ans = 0;
		
		for(int t=0;t<K;t++) { // k번 반복
			
			for(Fireball now: list) {
				int nx = (now.x + N + ((now.s % N) * dx[now.d])) % N;
				int ny = (now.y + N + ((now.s % N) * dy[now.d])) % N;
				
				now.x = nx;
				now.y = ny;
				map[nx][ny].add(now);
			}
			
			for(int i=0;i<N;i++)
				for(int j=0;j<N;j++) {
					if(map[i][j].size() < 2) {
						map[i][j].clear();
						continue;
					}
					
					int mSum = 0, sSum = 0;
					int check = map[i][j].get(0).d % 2;
					boolean flag = true;

					for(Fireball now: map[i][j]) {
						mSum += now.m;
						sSum += now.s;
						if(now.d%2 != check) 
							flag = false;
						list.remove(now);
					}

					int newMass = mSum / 5;
					int size = map[i][j].size();
					map[i][j].clear();
					
					if(newMass == 0) continue;
					int newS = sSum / size;
					
					if(flag) { 	// 0 2 4 6
						for(int k = 0; k < 8; k += 2) {
							list.add(new Fireball(i, j, newMass, newS, k));
						}
					} else {
						for(int k = 1; k < 8; k += 2) {
							list.add(new Fireball(i, j, newMass, newS, k));
						}
					}
				}
		}

		for(Fireball now : list) ans += now.m;
		
		return ans;
	}
}
