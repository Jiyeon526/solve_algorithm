import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class 백준_9375 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int Test_case = sc.nextInt();
		
		while(Test_case > 0) {
			Test_case--;
			
			int n = sc.nextInt();
			ArrayList<String> type = new ArrayList<>(); //옷의 종류
			int N[] = new int[n]; //해당 종류의 옷 갯수
			
			for(int i=0;i<n;i++) {
				String name = sc.next();
				String num = sc.next();
				if(!type.contains(num)) { // 입력받은 옷이 type에 없다면
					type.add(num);
					N[type.indexOf(num)] = 1;
				}
				else {
					N[type.indexOf(num)]++;
				}
			}
			
			// 옷들을 뽑음
			int ans = 1;
			for(int i=0;i<type.size();i++) {
				// 옷을 안 뽑는 경우도 있으므로 +1
				ans *= (N[i] + 1);
			}
			// 아무것도 안뽑았을 경우가 있어서 ans-1
			System.out.println(ans-1);
			
		}
	}
	
}
