# JUNGOL 1037번 오류교정

### 문제설명

- 문제
  - 불리언 행렬의 각각의 열과 각각의 행이 짝수 합을 가질 때 패리티 성질을 가지고 있다고 하자.
  - 당신이 할일은 행렬의 정보를 읽어서 이것이 패리티 성질을 가지고 있는지 없는지 판단해야한다. 만약 그렇지 않을 경우 하나의 비트를 바꿔서 이 행렬이 패리티 성질을 가질 수 있는가 확인하고 그렇지 않을 경우 행렬은 잘못된 행렬이라고 판단한다. 
- 입력
  - 첫줄에는 행렬의 크기인 n(n<100) 이 입력되며 n개의 줄에 n개의 0혹은 1이 입력된다.
- 출력
  - 만약 행렬이 패리티 성질을 가질 경우 __"OK"__라 출력하고 하나의 비트만을 변경해서 패리티 성질을 가질 경우 바꿔야 될 비트가 있는 i행 j열 에 대해 __"Change bit (i,j)"__ 라 출력하며 두 경우에 해당되지 않을 때는 __"Corrupt"__라고 출력한다. 
  - 각각의 행과 열은 1부터 시작한다.



### :neutral_face: 내가 푼 답

```java
import java.util.Arrays;
import java.util.Scanner;

public class jungol_1037 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int map[][] = new int[N+1][N+1];
		// 만약 홀수라면 해당 인덱스 저장해놓기
		int row[] = new int[N+1];
		int col[] = new int[N+1];
		
		// 입력받으면서 행의 합을 세서 합이 홀수라면 row배열에 인덱스 추가
		for(int i=1, x=0;i<N+1;i++) {
			int sum = 0;
			for(int j=1;j<N+1;j++) {
				map[i][j] = sc.nextInt();
				sum += map[i][j];
			}
			if(sum%2 == 1)
				row[x++] = i;
		}
		
		// 열의 합을 세서 홀수라면 col배열에 인덱스 추가
		for(int j=1, y=0;j<N+1;j++) {
			int sum = 0;
			for(int i=1;i<N+1;i++)
				sum += map[i][j];
			if(sum%2 == 1)
				col[y++] = j;
		}
		
		for(int i=0;i<N;i++) {
			// 만약 row, col 처음이 다 0이고 인덱스가 0이면 패리티 성질
			if(row[i] == 0 && col[i] == 0 && i == 0) {
				System.out.println("OK");
				break;
			}
			// 둘중 하나가 0이면 하나 고쳐도 패리티 안됨
			else if(row[i] == 0 || col[i] == 0) {
				System.out.println("Corrupt");
				break;
			}
			else {
				// 비트 하나 고쳐서 패리티 성질인지 확인
				boolean flag = true;
				map[row[i]][col[i]] = map[row[i]][col[i]] == 0?1:0;
				
				for(int a=1, x=0;a<N+1;a++) {
					int sum = 0;
					for(int j=1;j<N+1;j++) {
						sum += map[a][j];
					}
					if(sum%2 == 1) {
						flag = false;
						break;
					}
						
				}
				
				for(int j=1, y=0;j<N+1;j++) {
					int sum = 0;
					for(int a=1;a<N+1;a++)
						sum += map[a][j];
					if(sum%2 == 1) {
						flag = false;
						break;
					}
				}
				
				if(flag) {
					System.out.println("Change bit (" + row[i] + "," + col[i] + ")");
					break;
				}
				else
					map[row[i]][col[i]] = map[row[i]][col[i]] == 0?1:0;
				
			}
		}
	}
}
```

- 접근: 홀수인 행과 열의 인덱스를 받아서 저장하고 하나씩 바꾸면서 패리티 성질인지 확인, 그리고 인덱스 받은 길이가 서로 같지않다면 패리티 성질이 못됨. 이렇게 생각하고 풀었다.



### :+1: 다른 풀이

- 내가 생각하지 못했던것: 하나의 비트만 바꿔서 패리티 성질이 되려면 홀수인 행과 열의 인덱스를 받았을 때 그 갯수가 1개씩이여야된다.
- 코드

```java
import java.util.Arrays;
import java.util.Scanner;

public class jungol_1037 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int map[][] = new int[N+1][N+1];
		int row = 0;
		int col = 0;
		// row와 col에 값이 있는데 또 값이 들어올경우는 비트 바꿔도 패리티 성질이 아님
		boolean flag = true;

		for(int i=1;i<N+1;i++) {
			int sum = 0;
			for(int j=1;j<N+1;j++) {
				map[i][j] = sc.nextInt();
				sum += map[i][j];
			}
			if(sum%2 == 1 && row == 0)
				row = i;
			else if(sum%2 == 1)
				flag = false;
		}
		
		for(int j=1;j<N+1;j++) {
			int sum = 0;
			for(int i=1;i<N+1;i++)
				sum += map[i][j];
			if(sum%2 == 1 && col == 0)
				col = j;
			else if(sum%2 == 1)
				flag = false;
		}
		
		
		if(row == 0 && col == 0) 
			System.out.println("OK");
		else if(!flag)
			System.out.println("Corrupt");
		else
			System.out.println("Change bit (" + row + "," + col + ")");
	}

}
```

