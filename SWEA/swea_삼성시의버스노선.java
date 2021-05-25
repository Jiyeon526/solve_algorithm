import java.util.Scanner;

public class swea_삼성시의버스노선 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int tc=1;tc<TC+1;tc++) {
			int N = sc.nextInt();
			int bus[] = new int[5001];
			
			for(int i=0;i<N;i++) {
				int A = sc.nextInt();
				int B = sc.nextInt();
				for(int line=A;line<=B;line++)
					bus[line]++;
			}
			
			String ans = "#" + tc + " ";
			int P = sc.nextInt();
			for(int i=0;i<P;i++) {
				int c = sc.nextInt();
				ans += bus[c] + " ";
			}
			System.out.println(ans);
		}

	}

}
