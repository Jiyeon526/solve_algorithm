# SWEA 규영이와 인영이의 카드게임

### 문제설명

- 문제
  - 규영이와 인영이는 1에서 18까지의 수가 적힌 18장의 카드로 게임을 하고 있다. 한 번의 게임에 둘은 카드를 잘 섞어 9장씩 카드를 나눈다.
  - 높은 수가 적힌 카드를 낸 사람은 두 카드에 적힌 수의 합만큼 점수를 얻고, 낮은 수가 적힌 카드를 낸 사람은 아무런 점수도 얻을 수 없다. 이렇게 아홉 라운드를 끝내고 총점을 따졌을 때, 총점이 더 높은 사람이 이 게임의 승자가 된다.
  - 이 때, 규영이가 이기는 경우와 지는 경우가 총 몇 가지 인지 구하는 프로그램을 작성하라.
- 입력
  - 규영이의 카드 9장이 주어지며, 규영이는 정수가 주어지는 순서대로 카드를 낸다고 생각하면 된다.
- 출력
  - 인영이가 카드를 내는 9! 가지의 경우에 대해 규영이가 게임을 이기는 경우의 수와 게임을 지는 경우의 수를 공백 하나로 구분하여 출력한다.



### :full_moon_with_face: 내가 푼 답

```java
import java.util.Arrays;
import java.util.Scanner;

public class swea_규영이와인영이의카드게임 {
	
	// 기록(?)에 필요한 부분만 static 변수로 빼줌
	static int[] yin_game_card;
	static int[] gyu_card;
	static int win, lose;
	
	static void Select(int cnt, int[] yin_card, boolean[] isSelected) {
		// 카드를 9개 다뽑았으면 비교
		if(cnt == 10) {
			// 규영이의 점수와 인영이의 점수
			int gyu_sum = 0, yin_sum = 0;
			
			for(int i=1;i<10;i++)
				// 카드들을 비교해서 더 높은 숫자에다가 숫자들의 합을 저장
				if(gyu_card[i] > yin_game_card[i])
					gyu_sum += gyu_card[i] + yin_game_card[i];
				else if(gyu_card[i] < yin_game_card[i])
					yin_sum += gyu_card[i] + yin_game_card[i];
			
			// 점수들을 비교해서 규영이가 이겼으면 win, 졌으면 lose에 1씩더한다.
			if(gyu_sum > yin_sum)
				win++;
			else if(gyu_sum < yin_sum)
				lose++;
			return;
		}
		
		for(int i=1;i<10;i++) {
			// 만약에 인영이의 카드에서 뽑은 숫자가 이미 선택됐다면 넘어간다.
			if(isSelected[yin_card[i]])
				continue;
			// 선택했다고 바꿔주고
			isSelected[yin_card[i]] = true;
			// 인영이의 카드 조합 배열에 숫자를 넣어준다.
			yin_game_card[cnt] = yin_card[i];
			// 카드를 9개 선택할때까지 계속 한다.
			Select(cnt+1, yin_card, isSelected);
			isSelected[yin_card[i]] = false;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for(int tc=1;tc<TC+1;tc++) {
			// 전체 카드 저장
			int card[] = new int[19];
			// 규영이의 카드들을 저장
			gyu_card = new int[10];
			// 인영이의 카드들을 저장
			int yin_card[] = new int[10];
			
			// 규영이의 카드 번호를 입력받고
			for(int i=1;i<10;i++) {
				gyu_card[i] = sc.nextInt();
				// 규영이가 있는 카드번호를 전체 카드번호에서 체크를 해준다(1이 있음, 0은 없음)
				card[gyu_card[i]] = 1;
			}
			
			for(int i=1,j=1;i<19;i++)
				// 전체 카드들 중에 규영이가 가지고 있지 않은 번호(0으로 체크한 값들)를 인영이한테 넣어준다.
				if(card[i] == 0)
					yin_card[j++] = i;
			
			// 카드를 뽑았는지 안뽑았는지 체크
			boolean isSelected[] = new boolean[19];
			// 인영이의 카드들의 조합들을 저장
			yin_game_card = new int[10];
			win = 0;
			lose = 0;
			// 인영이의 카드 조합을 만드는 함수
			Select(1, yin_card, isSelected);
			System.out.println("#" + tc + " " + win + " " + lose);
		}
	}
}
```





#### :cake: 문제를 풀면서

- 오늘 처음으로 순열을 재귀로 풀어봤다. 그전에는 for문을 통해서만 구현을 해봤는데 재귀로 구현하면서 신기하기도하고 조금은 어려웠다!