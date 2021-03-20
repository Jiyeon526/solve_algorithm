import java.util.Scanner;

public class 백준_15829 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int L = sc.nextInt();
		String alp = sc.next();
		long hash = 0, pow[] = new long[50];	
		pow[0] = 1;
		
		for(int i=1;i<50;i++) {
			pow[i] = (pow[i-1] * 31) % 1234567891;
		}
		
		for(int i=0;i<L;i++) {
			long num = ((alp.charAt(i) - 'a' + 1) * pow[i]) % 1234567891;
			hash += num;
			if(hash > 1234567891)
				hash %= 1234567891;
		}
		System.out.println(hash);
	}

}

// 31의 제곱일때 오버플로우 나는거