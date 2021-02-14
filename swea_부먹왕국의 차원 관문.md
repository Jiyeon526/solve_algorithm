# SWEA 부먹왕국의 차원 관문

### 문제설명

- 문제
  - 어느 도시에 차원 관문을 설치하면 그 도시와 거리 D 이하인 다른 도시에서 차원 관문이 있는 곳으로 들어오거나, 혹은 차원 관문에서 거리 D 이하인 다른 도시로 나가는것이 가능하다.
  - 찍먹 왕국의 재침공에 대비하기 위해서 모든 도시 이동이 되어야하며 모든 차원 관문 사이와 직접적으로 이동이 가능하도록 차원 관문을 재건하려고 한다. (단, 0번 위치와 N+1번 위치에는 차원 관문이 존재 한다.) 
  - 가능한 빠른 건설을 위하여 최소 개수로 설치하는 계획을 세우려고 할때 도시들마다 차원관문이 남아있는 지에 대한 정보가 주어졌을 때, 이동에 필요한 차원관문의 최소 개수를 구하여라.
- 입력
  - 각 테스트 케이스의 첫 번째 줄에는 부먹 왕국의 도시 수 N(1 ≤ N ≤ 300,000)과 이동 제한 거리 D(1 ≤ D ≤ N)이 주어진다.
  - 1은 남아있음을 의미하며 0은 파괴 당한 것을 의미한다.
- 출력
  - 각 테스트 케이스마다 부먹 왕국이 추가로 건설 해야 하는 차원관문 의 최소 개수를 구하여라.



### :full_moon_with_face: 내가 푼 답

```java
import java.util.Scanner;

public class swea_부먹왕국의차원관문 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int tc=1;tc<TC+1;tc++) {
			int N = sc.nextInt();
			int D = sc.nextInt();
			int city[] = new int[N];	
			
			for(int i=0;i<N;i++)
				city[i] = sc.nextInt();
			
			int count = 0;
			int idx = 0;
			if(city[idx] == 0) {
				count++;
				city[idx] = 1;
			}
			
			while(idx < N) {
				int idx_clone = idx;

				if(D+idx >= N) {
					if(city[N-1] == 0)
						count++;
					break;
				}
				
				for(int j=D+idx;j>=idx+1;j--)
					if(city[j] == 1) {
						idx = j;
						break;
					}
				
				if(idx_clone == idx) {
					idx = idx + D;
					count++;
					city[idx] = 1;
				}
			}
			
			System.out.println("#" + tc + " " + count);
			
			
		}

	}

}
```



#### :grey_question: 궁금

- 나는 시간이 700ms가 나왔는데 다른 사람은 200ms이다...? 코드를 봐도 이해가 안된다.. 어떻게 생각한건지......