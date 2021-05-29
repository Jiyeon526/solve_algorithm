import java.util.Scanner;

public class swea_부먹왕국의차원관문 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int tc=1;tc<TC+1;tc++) {
			int N = sc.nextInt();
			int D = sc.nextInt();
			int city[] = new int[N];	
			
			for(int i=0;i<N;i++)
				city[i] = sc.nextInt();
			
			int count = 0;
			int idx = 0;
			if(city[idx] == 0) {
				count++;
				city[idx] = 1;
			}
			
			while(idx < N) {
				int idx_clone = idx;

				if(D+idx >= N) {
					if(city[N-1] == 0)
						count++;
					break;
				}
				
				for(int j=D+idx;j>=idx+1;j--)
					if(city[j] == 1) {
						idx = j;
						break;
					}
				
				if(idx_clone == idx) {
					idx = idx + D;
					count++;
					city[idx] = 1;
				}
			}
			
			System.out.println("#" + tc + " " + count);
			
			
		}

	}

}
