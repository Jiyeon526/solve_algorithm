import java.util.Scanner;

public class swea_테네스의특별한소수 {
	
	static boolean isPrime[] = new boolean[1000001];
	
	static void prime() {
		
		for(int i=0;i<1000000;i++)
			isPrime[i] = true;
		
		isPrime[0] = false;
		isPrime[1] = false;
		
		for(int i=2;i*i<=1000000;i++)
			for(int j=i*i;j<=1000000;j+=i)
				isPrime[j] = false;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		prime();
		
		for(int tc=1;tc<TC+1;tc++) {
			String D = sc.next();
			int A = sc.nextInt();
			int B = sc.nextInt();
			int cnt = 0;
			
			for(int i=A;i<=B;i++)
				if(isPrime[i]) {
					String c = Integer.toString(i);
					if(c.contains(D))
						cnt++;
				}
			System.out.println("#" + tc + " " + cnt);
		}

	}

}
