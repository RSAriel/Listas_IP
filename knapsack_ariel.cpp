#include <iostream>

using namespace std;

template
<typename T> void maximize(T &res, const T &val){
    if (res < val) res = val; 
    }

typedef long long ll;

int main()
{
    int cases;
    cin >> cases;
    while (cases--){
        int w, n;
        cin >> w;
        cin >> n ;

        int c[n + 1], v[n + 1];
        
        for (int i = 1; i <= n; ++i)
            cin >> c[i] >> v[i];

        ll f[n + 1][w + 1];

        for (int i = 0; i <= n; ++i) {
            fill(f[i], f[i] + w + 1, 0);
        }

        for (int i = 1; i <= n; ++i)
        {
            for (int s = 1; s <= w; ++s)
            {
                f[i][s] = f[i - 1][s];
                if (s >= c[i])
                {
                    maximize(f[i][s], f[i - 1][s - c[i]] + v[i]);
                }
            }
        }

        ll res = 0;
        for (int s = 0; s <= w; ++s)
            maximize(res, f[n][s]);

        cout << res;
    }
        return 0;
}