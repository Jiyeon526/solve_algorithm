# SWEA 의석이의 세로로 말해요

### 문제설명

- 문제
  - 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 의석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다. 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.
  - 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다.  세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.
- 입력
  - 각 테스트 케이스는 총 다섯 줄로 이루어져 있다.
  - 각 줄에는 길이가 1이상 15이하인 문자열이 주어진다. 각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.
- 출력
  - 각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 의석이가 세로로 읽은 순서대로 글자들을 출력한다.



### :full_moon_with_face: 내가 푼 답

```java
import java.util.Scanner;

public class swea_의석이의세로로말해요 {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();

        for(int tc=1;tc<TC+1;tc++) {
            char word[][] = new char[5][15];

            for(int i=0;i<5;i++) {
                String str = sc.next();
                word[i] = str.toCharArray();
            }

            String ans = "#" + tc + " ";
            for(int j=0;j<15;j++)
                for(int i=0;i<5;i++) {
                    if(word[i].length <= j)
                        continue;
                    ans += word[i][j];
                }
            System.out.println(ans);
        }
	}
}
```

- 풀이방법: 그냥 단순무식하게 풀었다. 배열 길이를 최대로 설정하고 그 자리에 값이 있다면 출력 아니면 출력안하는 방법이다.

#### :grey_question: 궁금한것

- 다른 방법은 없었을까..? 지금 내가 짠 코드는 배열의 길이가 길지않아서 괜찮았지만 만약에 엄청 길었다면..??

