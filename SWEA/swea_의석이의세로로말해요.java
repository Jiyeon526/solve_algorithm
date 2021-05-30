import java.util.Scanner;

public class swea_의석이의세로로말해요 {

	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int TC = sc.nextInt();
	
	for(int tc=1;tc<TC+1;tc++) {
		char word[][] = new char[5][15];
		
		for(int i=0;i<5;i++) {
			String str = sc.next();
			word[i] = str.toCharArray();
		}
		
		String ans = "#" + tc + " ";
		for(int j=0;j<15;j++)
			for(int i=0;i<5;i++) {
				if(word[i].length <= j)
					continue;
				ans += word[i][j];
			}
		System.out.println(ans);
				
	}

	}

}
