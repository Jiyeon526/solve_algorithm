#include <iostream>

using namespace std;

int room[15][15];

void room_person(){
	for(int i=0;i<15;i++)
		for(int j=0;j<15;j++){
			if(i == 0)
				room[i][j] = j+1;
			else if(j == 0)
				room[i][j] = 1;
			else
				room[i][j] = room[i][j-1]+room[i-1][j];
		}
}

int main(void){
	int test_case;
	
	cin >> test_case; 
	room_person();
	
	while(test_case>=1){
		int K, N;
		cin >> K >> N;
		
		cout << room[K][N-1] << endl;
		test_case--;
	}
	
	return 0;
}
