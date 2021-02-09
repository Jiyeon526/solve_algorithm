#include <iostream>

using namespace std;

int main(void){
	int test_case;
	
	cin >> test_case;
	
	while(test_case>=1){
		int H, W, N;
		cin >> H >> W >> N;
		int Y=N, X=1;
		
		while(true){
			Y-=H;
		//	cout << "Y = " << Y << " N = " << N << endl;
			if(Y<=0){
				cout << N << 0 << X << endl;
				break;
			}
			X++;
			if(Y<=H){
				cout << Y;
				if(X>=10)
					cout << X << endl;
				else
					cout << 0 << X << endl;
				break;
			}
		}
		
		test_case--; 
	}
	
	return 0;
}
