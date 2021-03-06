#メモ化再帰
#bitDPを使用する
#集合Sに訪問済みで頂点vにいるとしたときの頂点0まで戻るパスを考え、その経路長をdp[S][v]とする
#ここでSを長さVのビット列として考える

V,E = map(int, input().split())
INF = 10**10
cost = [[INF]*V for _ in range(V)] #重み
for e in range(E):
    s, t, d = map(int, input().split())
    cost[s][t] = d

dp = [[-1] * V for _ in range(1<<V)] # dp[S][v]

#メモ化再帰関数
def dfs(S, v, dp):
    if dp[S][v] != -1: #すでに訪問済みならメモを返す
        return dp[S][v]
    if S==(1<<V)-1 and v==0: #すべての頂点を訪れて頂点0に戻ってきた
        return 0 #もう動く必要がない
    
    res = INF
    for u in range(V):
        if S>>u & 1 == 0: #未訪問かどうか
            res = min(res, dfs(S|1<<u, u, dp)+cost[v][u])
    dp[S][v] = res
    return res

ans = dfs(0, 0, dp) #頂点0からスタートする。ただし頂点0は未訪問とする
if ans == INF:
    print(-1)
else:
    print(ans)