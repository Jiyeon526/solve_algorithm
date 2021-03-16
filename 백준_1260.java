import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 백준_1260 {
	static int num[][];
	static boolean visited[];
	static int N;
	static int M;
	static int V;
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());
		num = new int[N+1][N+1];
		visited = new boolean[N+1];
		
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(bf.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			num[to][from] = num[from][to] = 1;
		}
		
		visited[V] = true;
		dfs(V);
		System.out.println();
		Arrays.fill(visited, false);
		bfs();
		
	}
	public static void bfs() {
		Queue<Integer> q = new LinkedList<>();
		q.add(V);
		visited[V] = true;
		
		while(!q.isEmpty()) {
			int v = q.poll();
			System.out.print(v + " ");
			
			for(int i=1;i<N+1;i++)
				if(!visited[i] && num[v][i] == 1) {
					visited[i] = true;
					q.add(i);
				}
		}
	}
	
	public static void dfs(int v) {
		System.out.print(v + " ");
		
		for(int i=1;i<N+1;i++)
			if(!visited[i] && num[v][i] == 1) {
				visited[i] = true;
				dfs(i);
			}
		return;
	}
}
