import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class swea_키순서 {

	static int N;
	static ArrayList<ArrayList<Integer>> lst, revLst;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(bf.readLine());
		for(int t=1;t<=TC;t++) {
			N = Integer.parseInt(bf.readLine());
			int M = Integer.parseInt(bf.readLine());
			lst = new ArrayList<>();
			revLst = new ArrayList<>();
			
			for(int i=0;i<=N;i++) {// 초기화
				lst.add(new ArrayList<>());
				revLst.add(new ArrayList<>());
			}
			
			for(int i=0;i<M;i++) {
				StringTokenizer st = new StringTokenizer(bf.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				lst.get(a).add(b);
				revLst.get(b).add(a);
			}
			
			int ans = 0;
			for(int i=1;i<=N;i++) {
				int high = higher(i);
				int low = lower(i);
				if(high + low == N-1)
					ans++;
			}
			
			System.out.println("#" + t + " " + ans);
		}

	}

	private static int lower(int target) {
		int cnt = 0;
		Queue<Integer> q = new LinkedList<>();
		boolean[] visit = new boolean[N+1];
		q.add(target);
		visit[target] = true;
		
		while(!q.isEmpty()) {
			int now = q.poll();
			
			for(int i=0;i<revLst.get(now).size();i++) {
				if(!visit[revLst.get(now).get(i)]) {
					q.add(revLst.get(now).get(i));
					cnt++;
					visit[revLst.get(now).get(i)] = true;
				}
			}
		}
		
		return cnt;
	}

	private static int higher(int node) {
		int cnt = 0;
		Queue<Integer> q = new LinkedList<>();
		boolean[] visit = new boolean[N+1];
		q.add(node);
		visit[node] = true;
		
		while(!q.isEmpty()) {
			int now = q.poll();
			
			for(int i=0;i<lst.get(now).size();i++) {
				if(!visit[lst.get(now).get(i)]) {
					q.add(lst.get(now).get(i));
					cnt++;
					visit[lst.get(now).get(i)] = true;
				}
			}
		}
		
		return cnt;
	}

}
