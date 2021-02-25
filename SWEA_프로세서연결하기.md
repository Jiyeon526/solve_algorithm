# SWEA 프로세서 연결하기

### 문제설명

- 문제
- 입력
- 출력



### :full_moon_with_face: 내가 푼 답

```java

```



### 문제 풀이

- 첫번째 접근: 코어이면 상, 하, 좌, 우를 다 탐색해서 만약에 전선을 못놓으면 -1, 놓을 수 있으면 전선 수를 저장하고 코어의 상, 하 , 좌, 우 중 가장 작은값을 더해서 최소값을 찾았야지! 

- 문제점: __전선끼리 겹치지 못한다. __이걸 고려안하고해서 오류가 났다.

- 코드

  ```java
  static void search(int x, int y, int k) {
      boolean flag = true;
      int cnt = 0;
  
      //아래
      for(int i=x+1;i<N;i++) {
          if(board[i][y] == 1) {
              flag = false;
              break;
          }
          cnt++;
      }
      if(flag)
          core[k][0] = cnt;
      else
          core[k][0] = -1;
      flag = true; cnt = 0;
      
      // 생략
  }
  
  for(int i=0;i<n;i++){
      코어의 x, y좌표값 가져와서
      search(x, y, i);
  }
  
  int ans = 0;
  for(int i=0;i<n;i++) {
      int min = Integer.MAX_VALUE;
      System.out.println("i = " + i + Arrays.toString(core[i]));
      for(int j=0;j<4;j++) {
          if(core[i][j] == -1)
              continue;
          min = min>core[i][j]?core[i][j]:min;
      }
      ans += min;
  }
  ```

  