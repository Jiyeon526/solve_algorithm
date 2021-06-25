import java.util.Scanner;

public class 백준_1956_운동 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int V = sc.nextInt();
		int E = sc.nextInt();
		int[][] arr = new int[V+1][V+1];

		for(int i=0;i<V+1;i++)
			for(int j=0;j<V+1;j++)
				arr[i][j] = Integer.MAX_VALUE;
		
		for(int i=0;i<E;i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			
			arr[a][b] = c;
		}
		
		for(int k=1;k<V+1;k++)
			for(int i=1;i<V+1;i++)
				for(int j=1;j<V+1;j++) {
					if(arr[i][j] > arr[i][k] + arr[k][j])
						arr[i][j] =  arr[i][k] + arr[k][j];
				}
					
		
		for(int i=0;i<V+1;i++) {
			for(int j=0;j<V+1;j++)
				System.out.print(arr[i][j] + " ");
			System.out.println();
		}
		
		int ans = Integer.MAX_VALUE;
		for(int i=1;i<V+1;i++)
			ans = Math.min(arr[i][i], ans);
		
		if(ans == Integer.MAX_VALUE)
			System.out.println("-1");
		else
			System.out.println(ans);
		
	}
}
