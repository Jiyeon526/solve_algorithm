import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 백준_18111 {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int map[][] = new int[N][M];
		
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(bf.readLine());
			for(int j=0;j<M;j++)
				map[i][j] = Integer.parseInt(st.nextToken());
		}
		
		int time = Integer.MAX_VALUE, len = 0; // 최종 시간, 땅 높이
		for(int i=256;i>=0;i--) { // 땅 높이
			int now_time = 0;
			int inv_a = 0, inv_b = 0; // 쌓을때 필요한 블록 갯수, 뺄때의 블록 갯수
			for(int j=0;j<N;j++)
				for(int k=0;k<M;k++) {
					if(i == map[j][k]) //바꿀 땅 높이와 현재 땅 높이가 같다면
						continue;
					if(i > map[j][k]) { //블록을 쌓는 경우
						now_time += i - map[j][k];
						inv_a += i - map[j][k];
					}
					else if(i < map[j][k]) { //블록을 빼는 경우
						now_time += (map[j][k] - i)*2;
						inv_b += (map[j][k] - i);
					}
				}
			if(B+inv_b-inv_a >= 0) //땅 높이가 다 같음
				if(now_time < time) {
					time = now_time;
					len = i;
				}		
		}
		System.out.println(time + " " + len);
		
	}

}
