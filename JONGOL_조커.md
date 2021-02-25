# JONGOL 조커

### 문제설명

- 문제
  - N개의 숫자가 적힌 카드가 있다.  1, 2, 3, 4, 5를 뽑아서 순서대로 늘어놓을 경우 이는 길이 5의 스트레이트라고 한다.
  - 숫자 0 이 적힌 카드가 있는데 이는 조커라고 하며, 자신이 원하는 어떤 숫자로도 변환이 가능하다. 조커 카드와 일반 카드가 주어졌을 때 가장 긴 길이의 스트레이트를 만드는 프로그램을 작성하라.
- 입력
  - 입력의 첫 번째 줄에는 카드의 갯수 N(N≤1,000)이 입력된다. 그 다음 줄에는 N개의 카드에 적힌 숫자가 입력된다. 입력되는 카드에 적힌 숫자의 범위는 0 이상 1,000,000 이하이다. 0은 조커를 의미한다.
- 출력
  - 입력된 카드들을 가지고 만들 수 있는 스트레이트의 최대 길이를 출력한다.



### :full_moon_with_face: 내가 푼 답

```java
import java.util.Arrays;
import java.util.Scanner;

public class JUNGOL_조커 {

	static int[] set(int[] num, int zero_num, int N) {
		int[] newNum = new int[N];
		
		if(zero_num == N)
			return newNum;
		
		int pre = num[zero_num];
		newNum[0] = pre;
		int x = 1;
		
		for(int i=zero_num+1;i<N;i++) {
			if(pre == num[i])
				continue;
			newNum[x++] = num[i];
			pre = num[i];
		}
		
		return newNum;
	}
	
	static int count(int zero_num, int[] num, int N, int s) {
		int cnt = 1;
		int zero = zero_num;
		
		for(int i=s+1;i<N;i++) {
			if(num[i] == 0)
				break;
			if(num[i] - num[i-1] == 1)
				cnt++;
			else if(num[i] - num[i-1] - 1 <= zero) {
				cnt++;
				cnt += num[i] - num[i-1] - 1;
				zero -=  num[i] - num[i-1] - 1;
			}
			else
				break;
		}
		
		if(zero != 0)
			cnt += zero;
		
		return cnt;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int num[] = new int[N];
		int zero_num = 0;
		
		for(int i=0;i<N;i++) {
			num[i] = sc.nextInt();
			if(num[i] == 0)
				zero_num++;
		}
		
		Arrays.sort(num);
		num = set(num, zero_num, N);
		
		int max_len = Integer.MIN_VALUE;
		for(int i=0;i<N;i++) {
			if(i == 0 && num[i] == 0) {
				max_len = zero_num;
				break;
			}
			if(num[i] == 0)
				break;
			int len = count(zero_num, num, N, i);
			max_len = len>max_len?len:max_len;
		}
		
		System.out.println(max_len);
	}

}
```



### 문제 풀이 과정

- 접근:  숫자들을 정렬한다 :arrow_right: 0의 갯수를 세준다 :arrow_right: 숫자들의 중복을 제거한다. :arrow_right: 그 숫자들을 시작점으로 하나씩 스트레이트 길이를 검사한다.

- 문제점: 모든 카드가 0일때를 고려를 안했다 ㅜㅜ && 중복을 제거할때 배열의 범위를 넘어갈 수 있다.

- 해결: 밑의 코드를 추가해줘서 해결했다.

  ```java
  함수 set{
      int[] newNum = new int[N];
  		
  		if(zero_num == N)
  			return newNum;
      // 생략
  }
  
  main문{
      for(int i=0;i<N;i++) {
          // 모든 숫자가 0일때는 0의 갯수만큼 길이를 만들 수 있다.
          if(i == 0 && num[i] == 0) {
              max_len = zero_num;
              break;
          }
          // 생략
      }
  }
  ```





#### :globe_with_meridians: 출처

- http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=488&sca=99