# SWEA 테네스의 특별한 소수

### 문제 설명

- 문제
  - 테네스는 D를 포함하는 숫자도 좋아한다. 그렇기에 소수가 D를 포함하면 더욱 더 좋아하여 특별한 소수라고 부르기로 했다.
  - 예를 들어 D = 3이면 3, 13, 23, … 같은 소수들이 3을 포함하였으므로 테네스는 이런 숫자들을 특별한 소수라고 부를 것이다.
  - D가 주어질 때, A이상 B이하의 수 중에서 특별한 소수인 것들의 개수를 구하는 프로그램을 작성하라.
- 입력
  - 첫 번째 줄에 테스트 케이스의 수 T가 주어진다. 각 테스트 케이스의 첫 번째 줄에는 세 정수 D, A, B(1 ≤ D ≤ 9, 1 ≤ A ≤ B ≤ 106)가 공백으로 구분되어 주어진다.
- 출력
  - 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별한 소수의 개수를 출력한다.



### :full_moon_with_face: 내가 푼 답

```java
import java.util.Scanner;

public class swea_테네스의특별한소수 {
	
	static boolean isPrime[] = new boolean[1000001];
	
	static void prime() {
		
		for(int i=0;i<1000000;i++)
			isPrime[i] = true;
        
		//0과 1은 소수가 아니다
		isPrime[0] = false;
		isPrime[1] = false;
		
        //제곱의 수가 자기보다 작은 수일때만 지워도 충분하다
		for(int i=2;i*i<=1000000;i++)
            // 그 수의 제곱부터 시작해서 (2이면 4) j를 2씩 늘려주면
            //2의 배수들은 다 false로 변한다.
			for(int j=i*i;j<=1000000;j+=i)
				isPrime[j] = false;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		prime();
		
		for(int tc=1;tc<TC+1;tc++) {
			String D = sc.next();
			int A = sc.nextInt();
			int B = sc.nextInt();
			int cnt = 0;
			
			for(int i=A;i<=B;i++)
				if(isPrime[i]) {
					String c = Integer.toString(i);
					if(c.contains(D))
						cnt++;
				}
			System.out.println("#" + tc + " " + cnt);
		}

	}

}
```

- 이 문제는 에라토스테네스의 체를 모르면 조금 시간이 걸리지않을까 싶다! 

