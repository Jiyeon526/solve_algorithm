import java.util.Scanner;

public class 백준_2564 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int row = sc.nextInt();
		int col = sc.nextInt();
		int storeCnt = sc.nextInt();
		int[][] store = new int[storeCnt+1][3];

		for(int i=0;i<storeCnt+1;i++) {
			int d = sc.nextInt(), m = sc.nextInt();
			if(d == 1) {
				store[i][0] = 0;
				store[i][1] = m;
			}else if(d == 2) {
				store[i][0] = col;
				store[i][1] = m;
			}else if(d == 3) {
				store[i][0] = m;
				store[i][1] = 0;
			}else {
				store[i][0] = m;
				store[i][1] = row;
			}
			store[i][2] = d;
		}
		
		int rev = 0;
		if(store[storeCnt][2] == 1)
			rev = 2;
		else if(store[storeCnt][2] == 2)
			rev = 1;
		else if(store[storeCnt][2] == 3)
			rev = 4;
		else
			rev = 3;
		
		int cnt = 0;
		for(int i=0;i<storeCnt;i++) {
			if(rev == store[i][2]) {
				int tmp1 = 0, tmp2 = 0;
				if(store[i][2] <= 2) {
					cnt += col;

					tmp1 += store[i][1];
					tmp1 += store[storeCnt][1];
				
					tmp2 += row - store[i][1];
					tmp2 += row - store[storeCnt][1];
					
					cnt += Math.min(tmp1, tmp2);
				}else {
					cnt += row;

					tmp1 += store[i][0];
					tmp1 += store[storeCnt][0];
				

					tmp2 += col - store[i][0];
					tmp2 += col - store[storeCnt][0];
					
					cnt += Math.min(tmp1, tmp2);	
				}
				
			}
			else {
				cnt += Math.abs(store[storeCnt][0] - store[i][0]) + Math.abs(store[storeCnt][1] - store[i][1]);
			}
		}

		System.out.println(cnt);
	}

}
