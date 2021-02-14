# SWEA 원재의 메모리 복구

### 문제 설명

- 문제
  - 메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것이다.
  - 원래 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산해보자.
- 입력
  - 첫 번째 줄에 테스트 케이스의 수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 메모리의 원래 값이 주어진다. 메모리의 길이는 1이상 50이하이다.
- 출력
  - 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 초기값(모든bit가 0)에서 원래 값으로 복구하기 위한 최소 수정 횟수를 출력한다.



### :full_moon_with_face: 내가 푼 답

```java
import java.util.Scanner;

public class swea_원재의메모리복구 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int t=1;t<TC+1;t++) {
			String ans_bit = sc.next();
			char init_bit[] = new char[ans_bit.length()];
			
            // 배열 초기화
			for(int i=0;i<ans_bit.length();i++)
				init_bit[i] = '0';
			
            // 바뀐 수 세기
			int count = 0;
			for(int i=0;i<ans_bit.length();i++) {
				if(ans_bit.charAt(i) != init_bit[i]) {
					count++;
					for(int j=i;j<ans_bit.length();j++)
						if(init_bit[j] == '1')
							init_bit[j] = '0';
						else
							init_bit[j] = '1';
				}
			}
			System.out.println("#" + t + " " + count);
		}

	}

}
```

- 문제 접근: 처음 0으로 초기화된 배열과 답을 비교하면서 왼쪽에 있는 숫자가 1로 바뀌면 그건 무조건 바뀌어야된다고 생각하고 풀었다. 