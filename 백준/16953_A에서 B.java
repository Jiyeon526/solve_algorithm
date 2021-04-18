package 백준특강;

import java.util.Scanner;

public class 백준_16953 {
	static long a, b;
	static boolean check;
	
	public static void dfs(long nowNum, int cnt) {
		if(nowNum == b) {
			System.out.println(cnt+1);
			check = true;
			return;
		}else if(nowNum > b) return;
		
		dfs(nowNum*2, cnt+1);
		
		long n = (nowNum * 10) + 1;
		dfs(n, cnt+1);

	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		a = sc.nextInt();
		b = sc.nextInt();
		check = false;
		dfs(a, 0);
		
		if(!check)
			System.out.println("-1");
	}

}
