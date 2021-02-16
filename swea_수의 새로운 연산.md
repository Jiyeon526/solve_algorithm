# SWEA 수의 새로운 연산

### 문제 설명

- 문제
  - 2차원 평면 제 1사분면 위의 격자점 (x,y)에 위 그림과 같이 대각선 순서로 점에 수를 붙인다.  점 (x,y)에 할당된 수는 #(x,y)로 나타낸다.
  - 반대로 수 p가 할당된 점을 &(p)로 나타낸다. 두 점에 대해서 덧셈을 정의한다. 점 (x,y)와 점 (z,w)를 더하면 점 (x+z, y+w)가 된다.
  - 우리가 해야 할 일은 수와 수에 대한 새로운 연산 ★를 구현하는 것으로, p★q는 #(&(p)+&(q))으로 나타난다.
- 입력
  - 첫 번째 줄에 테스트 케이스의 수 T가 주어진다. 각 테스트 케이스의 첫 번째 줄에는 두 정수 p,q(1 ≤ p, q ≤ 10,000)가 주어진다.
- 출력
  -  테스트 케이스마다 ‘#t’(t는 테스트 케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 각 테스트 케이스마다 p★q의 값을 출력한다.



### :full_moon_with_face: 내가 푼 답

```java
import java.util.Scanner;

public class swea_수의새로운연산 {

	public static void main(String[] args) {
		long[][] N = new long[350][350];
		// 1부터 저장, 한번 저장할때 이동거리
		long num = 1, D = 1;
		// 좌표
		int i = 0, j = 0;
		
		while(i<350) {
			for(int d=0;d<D;d++) {
				N[i][j] = num;
				// i는 위로 한칸, j는 오른쪽으로 한칸씩 이동
				i--;
				j++;
				num++;
			}
			// i를 j값으로 바꿔주면 대각선으로 이동할 수 있음
			i = j;
			j = 0;
			D++;
		}
		
		
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int tc=1;tc<TC+1;tc++) {
			int p = sc.nextInt();
			int q = sc.nextInt();
			
			// x좌표의 합, y좌표의 합, end는 p와 q를 찾았는지 체크
			int sum_x = 0, sum_y = 0, end=0;
			
			for(int x=0;x<350 && end<=2;x++)
				for(int y=0;y<350 && end<=2;y++) {
					if(N[x][y] == p) {
						// 찾으면 값을 저장
						sum_x += x;
						sum_y += y;
						// 값 2개를 다 찾으면 for문을 수행할 필요가 없음
						end++;
					}
					if(N[x][y] == q) {
						sum_x += x;
						sum_y += y;
						end++;
					}
					
				}
			// 출력
			System.out.println("#" + tc + " " + N[sum_x+1][sum_y+1]);
			
		}

	}

}
```



### 문제 풀이 과정

- 처음에는 p와 q를 같은 조건문에 넣었는데 이러면 p와 q가 같을때는 한번밖에 수행을 안해서 오류가 난다.

```java
for(int x=0;x<350 && end<=2;x++)
    for(int y=0;y<350 && end<=2;y++) {
        if(N[x][y] == p || N[x][y] == q) {
            sum_x += x;
            sum_y += y;
            end++;
        }
```

- 그래서 위의 답에 있는 코드처럼 if문을 2개를 줘서 해결했다.