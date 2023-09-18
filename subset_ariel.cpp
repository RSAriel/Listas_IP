#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> dp;

int findNoOfSubsets(int *A, int N, int i, int sum) {

    if (i == N) {
        if (sum == 0)
            return 1;
        else
            return 0;
    }
    
    if(sum<0)
		return 0;
		

    if (dp[i][sum] != -1)
        return dp[i][sum];
        
    int take = 0, notTake = 0;
    take = findNoOfSubsets(A, N, i + 1, sum - A[i]);
    notTake = findNoOfSubsets(A, N, i + 1, sum);
    

    return dp[i][sum] = (take + notTake);
}


int main(){
    int cases, tamanho, soma;
    cin >> cases;
    while(cases--){
        cin >> tamanho;
        int array[tamanho];

        for(int i = 0; i < tamanho; ++i){
            cin >> array[i];
        }
        cin >> soma;

        int N = sizeof(array) / sizeof(int);

        dp.resize(N + 1, vector<int>(soma + 1, -1));
        cout << findNoOfSubsets(array, N, 0, soma) << endl;
    }
    return 0;
}