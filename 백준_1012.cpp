#include <iostream>

using namespace std;

bool visit[51][51];
int dx[] = {0,0,-1,1};
int dy[] = {1,-1,0,0};
int map[51][51];
int M, N;

void dfs(int start, int end){
	//queue<int> q;
	visit[start][end] = true;
	
	//while(!q.empty()){
	//	int size = q.size();
		
		for(int i=0;i<4;i++){
			int x = dx[i]+start;
			int y = dy[i]+end;
			if(x<0 || y<0 || x>=M || y>=N)
				continue;
			if(map[x][y] == 0 || visit[x][y])
				continue;
			
			dfs(x, y);
		}
				
	//}
}
int main(void){
	int T, K;
	
	cin >> T;
		
	for(int i=0;i<T;i++){
		cin >> M >> N >> K;
		int cnt = 0, x=0, y=0;
		
		for(int i=0;i<50;i++)
			for(int j=0;j<50;j++){
				map[i][j] = 0;
				visit[i][j] = false;
			}
			
		for(int i=0;i<K;i++){
			cin >> x >> y;
			map[x][y] = 1;
		}
		
		for(int i=0;i<M;i++)
			for(int j=0;j<N;j++)
				if(map[i][j] == 1 && !visit[i][j]){
					cnt++;
					dfs(i, j);
				}
				
		cout << cnt <<endl;
	}
	
	return 0;
}
