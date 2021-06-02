import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 백준_2239 {
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int[][] map = new int[9][9];
		
		for(int i=0;i<9;i++) {
			String s = bf.readLine();
			for(int j=0;j<9;j++) {
				map[i][j] = s.charAt(j) - '0';
			}
		}
		
		int[][] h_check = new int[9][10];
		int[][] v_check = new int[9][10];
		int[][] s_check = new int[9][10];
		
		for(int i=0;i<9;i++)
			for(int j=0;j<9;j++) {
				if(map[i][j] != 0)
					h_check[i][map[i][j]] = 1;
				if(map[j][i] != 0)
					v_check[i][map[j][i]] = 1;
			}
		
		for(int j=0;j<9;j++)
			for(int k=0;k<9;k++) {
				int s = find(j, k);
				if(map[j][k] != 0)
					s_check[s][map[j][k]] = 1;
			}

		
		make(map, v_check, s_check, h_check);
		
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++)
				System.out.print(map[i][j]);
			System.out.println();
		}
	}
	
	public static boolean make(int[][] map,int[][] v_check,int[][] s_check,int[][] h_check) {	

		for(int i=0;i<9;i++)
			for(int j=0;j<9;j++)
				if(map[i][j] == 0) {
					for(int k=1;k<10;k++) {
						int idx = find(i, j);
						if(h_check[i][k] == 0 && v_check[j][k] == 0 && s_check[idx][k] == 0) {
							h_check[i][k] = v_check[j][k] = s_check[idx][k] = 1;
							map[i][j] = k;
							if(make(map, v_check, s_check, h_check)) return true;
							h_check[i][k] = v_check[j][k] = s_check[idx][k] = 0;
						}	
					}	
					map[i][j] = 0;
					return false;
				}
	
		return true;
	}
	
	private static boolean isComplete(int[][] map) {
		for(int i=0;i<9;i++)
			for(int j=0;j<9;j++)
				if(map[i][j] == 0)
					return false;
		return true;
	}

	public static int find(int i, int j) {
		if(i<=2) {
			if(j<=2) return 0;
			if(j<=5) return 1;
			return 2;
		}else if(i<=5) {
			if(j<=2) return 3;
			if(j<=5) return 4;
			return 5;
		}else {
			if(j<=2) return 6;
			if(j<=5) return 7;
			return 8;
		}
	}

}