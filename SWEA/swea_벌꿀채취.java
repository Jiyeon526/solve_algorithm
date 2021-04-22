import java.util.Arrays;
import java.util.Scanner;

public class swea_벌꿀채취 {

	static int N, M, C, sum;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		for(int t=1;t<=TC;t++) {
			N = sc.nextInt();
			M = sc.nextInt();
			C = sc.nextInt();
			int[] honey = new int[N*N];
			int[] profit = new int[N*N];
			
			for(int i=0;i<N;i++)
				for(int j=0;j<N;j++)
					honey[i*N+j] = sc.nextInt();

			for(int i=0;i<N*N;i++) {
				boolean flag = true;
				int[] a = new int[M];
				
				for(int j=i,x=0;j<i+M;j++) {
					if(j != i && j%N == 0) { //이차원 배열로 생각했을때 가로 인덱스가 M을 넘어가면 안되기때문
						flag = false;
						break;
					}
					a[x++] = honey[j];
				}

				if(flag) { // a배열에 다 담겼을때만 수익 계산
					sum = 0;
					makeProfit(a, 0, new boolean[M]);
					profit[i] = sum;
				}
			}

			// 최대 수익 2개 선택하기
			int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE;
			for(int i=0;i<N*N;i++) { // 기준점
				int tmp = (i+1)%N==0?i+1:i+M; // 만약에 가로 인덱스가 M-1이면 다음 수를 선택할 수 있기 때문
				int max = Integer.MIN_VALUE;
				
				for(int j=tmp;j<N*N;j++) { // 최대가 profit[i]라고 생각했을때 i와 안 겹치는 범위에서 최대 수익 계산 
					max = Math.max(max, profit[j]);
				}
				
				if(max1 + max2 < max + profit[i]) { // 만약 둘의 합이 더 크다면 갱신
					max1 = profit[i];
					max2 = max;
				}
			}
			
			System.out.println("#" + t + " " + (max1 + max2));
		}

	}

	private static void makeProfit(int[] pot, int idx, boolean[] visit) { // a배열 최대 수익 계산
		if(idx == M) {
			int res = 0;
			int resSum = 0; // 뽑은 수들의 합
			
			for(int i=0;i<M;i++)
				if(visit[i])
					resSum += pot[i];

			if(resSum > C) return; // 만약에 합이 C를 넘어간다면 그냥 리턴(사용 못함)
			
			for(int i=0;i<M;i++)
				if(visit[i])
					res += Math.pow(pot[i], 2); // 수익 계산
			
			sum = Math.max(sum, res); // 최대 수익 갱신
			return;
		}else if(idx > M) return;
		
		// 부분 집합 사용
		visit[idx] = true;
		makeProfit(pot, idx+1, visit);
		visit[idx] = false;
		makeProfit(pot, idx+1, visit);
	}
}
