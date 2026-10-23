typedef long long ll;
ll f[1<<16][16];
class Solution {
public:
    ll elevatorRequests(int n, int start, vector<vector<int>>& R) {
        for(int i=0;i<(1<<R.size());++i)
            for(int j=0;j<R.size();++j) f[i][j]=1e18;
        f[0][0]=0;
        ll ans=0;
        for(int i=0;i<(1<<R.size());++i) {
            ll mi = 1e13;
            for(int j=0;j<R.size();++j) {
                ll O=i?R[j][1]:int(start);
                mi=min(mi,f[i][j]);
                for(int k=0;k<R.size();++k)if(i&(1<<k));else {
                f[i|(1<<k)][k]=min(f[i|(1<<k)][k],max(f[i][j]+abs(O-R[k][1]),(ll)R[k][0]));
                }
            }
            ans=mi;
        }
        return ans;
    }
};