import java.util.Scanner;

public class SWEA_조합 {
	static final int MOD = 1234567891;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int t=1;t<=TC;t++) {
			long N = sc.nextInt();
			long R = sc.nextInt();
			
			long tmpN = f(N);
			long a = (f(R) * f(N-R)) % MOD;
			long b = pow(a, MOD-2);
			long ans = (tmpN * b) % MOD;

			System.out.println("#" + t + " " + ans);
		}

	}
	
	public static long pow(long n, int p) { // 제곱 계산
		if(p == 0) return 1;
	
		long tmp = pow(n, p/2);
		long res = (tmp * tmp) % MOD;
		if(p%2 == 0) {
			return res;
		}
		return (res * n) % MOD;
		
	}
	
	public static long f(long n) { // 팩토리얼 계산
		if(n == 0) return 1;
		
		long x = 1;
		for(int i=2;i<=n;i++)
			x = (x*i) % MOD;
		return x;
	}

}
