# SWEA 성공적인 공연 기획

### 문제설명

- 문제 
  - 각 사람들의 조건이 모두 다르기 때문에, 구성이 어떤 지에 따라 몇몇의 사람은 기립 박수를 하지 않을 수도 있다. 
  - 몇 명의 사람들을 고용하여 공연이 끝난 후 기립 박수를 바로 하게 하여 실제로 표를 사서 공연을 관람한 사람들이 모두 기립 박수를 하도록 하게 하고 싶다. 최소 몇 명의 사람들을 따로 고용해야 할까?
- 입력
  - 각 테스트 케이스의 첫 번째 줄에는 ‘0’에서 ‘9’사이의 문자 만으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1001 이하이다.
  - 첫 번째 글자가 의미하는 바는 기립 박수를 하고 있는 사람이 아무도 없을 때(0 명일 때) 기립 박수를 하는 사람의 수를 의미한다.
  - i번째 글자가 의미하는 바는 기립 박수를 하고 있는 사람이 i-1명 이상일 때 기립 박수를 하는 사람의 수를 의미한다.
- 출력
  - 모든 관객이 기립 박수를 하게 하려면 최소 몇 명의 사람을 고용해야 하는지 출력한다.



### :full_moon_with_face: 내가 푼 답

```java
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
```



### :question: 이해가 안되는것

- 해당 코드를 다음과 같이 바꿨더니 안된다. 근데 내 논리로는 둘이 같은 코드인데 안되는게 이상하다.

```java
// 답 코드
if(people_sum >= i)
	people_sum += people[i];
else {
	need_people += i - people_sum;
	people_sum = i + people[i];
}

// 내가 바꾼 코드(이해가 안됨. 왜 이렇게 바꾼거는 안되는건지)
if(people_sum < i) {
    need_people += i - people_sum;
    people_sum += i;
}
people_sum += people[i];
```





#### :globe_with_meridians: 출처

- https://swexpertacademy.com/main/solvingProblem/solvingProblem.do