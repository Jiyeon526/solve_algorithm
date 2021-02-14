# SWEA 농작물 수확하기

### 문제설명

- 문제
  - 농장의 크기는 NxN(N은 항상 홀수), 마름모 모양의 농작물을 수확할때 그 가치는?
- 입력
  - 각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.
- 출력
  - 각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.



### :full_moon_with_face: 내가 푼 답

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class swea_농작물수확하기 {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(bf.readLine());
		
		for(int tc=1;tc<TC+1;tc++) {
			int N = Integer.parseInt(bf.readLine());
			char farm[][] = new char[N][N];
			
			for(int i=0;i<N;i++) {
				String str = bf.readLine();
				farm[i] = str.toCharArray();
			}

			int sum = 0;
			for(int i=0;i<N/2+1;i++) {
				for(int j=N/2-i;j<(2*i+1)+(N/2-i);j++) {
					sum += farm[i][j] - 48;
				}
				
				if(i != N/2)
					for(int j=i+1;j<N-(i+1);j++) {
						sum += farm[i+N/2+1][j] - 48;
					}
			}
			
			System.out.println("#" + tc + " " + sum);
					
			
		}
	}

}
```



#### :cake: 문제를 풀면서

- 이 문제는 범위를 설정하는 것보다 입력을 받을때 bufferedreader를 처음 쓰다보니 어려웠다. 위에 코드를 보면 깔끔(?)하게 입력받지못하고 char를 이용해서 풀었다. 나중에 int로 받아서 푸는 방법을 공부해야겠다.



#### :globe_with_meridians: 출처

- https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXdbtMcKyWIDFAUO&contestProbId=AV7GLXqKAWYDFAXB&probBoxId=AXdlPMIKObYDFAUO&type=PROBLEM&problemBoxTitle=day0203&problemBoxCnt=3