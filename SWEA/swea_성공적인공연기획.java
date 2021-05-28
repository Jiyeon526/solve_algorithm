import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class swea_성공적인공연기획 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		
		for(int tc=1;tc<TC+1;tc++) {
			String str = br.readLine();
			int people[] = new int[str.length()];
			
			// 입력
			for(int i=0;i<str.length();i++)
				people[i] = str.charAt(i) - 48;
			
			// 박수친 사람의 합
			int people_sum = people[0];
			// 박수치는데 필요한 사람
			int need_people = 0;
			for(int i=1;i<people.length;i++) {
				// 만약 0이라면 그냥 넘어간다(박수안쳐도됨)
				if(people[i] == 0)
					continue;
				// 지금까지 박수친 사람의 합이 필요한 사람 수 이상이라면 박수치는사람을 합한다.
				if(people_sum >= i)
					people_sum += people[i];
				else {
					// 그렇지않다면 필요한 사람은 현재 총 필요한 사람수(i)에서 지금까지 박수친 사람을 빼면 나온다. 
					need_people += i - people_sum;
					// 총 박수친 사람은 필요한 사람수에 박수치는사람의 합이다.
					people_sum = i + people[i];
				}
			}
			System.out.println("#" + tc + " " + need_people);
		}
	}

}
