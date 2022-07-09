import math


class SegmentTree(object):
    INF = 1 << 15 - 1
    MAX_N = 10**4

    def __init__(self, n):
        # 区間の始めの線分を垂直とした時の最後の線分の端点までのベクトル
        self.vx = [self.INF]*self.MAX_N
        self.vy = [self.INF]*self.MAX_N
        # 各節点の角度
        self.ang = [self.INF]*self.MAX_N

        self.n = n

        self.create_node(0, 0, n)
    
    def create_node(self, k, l, r):
        """ノードの初期化

        Args:
            k (int): 節点の番号
            l, r (int): 区間
        """
        self.ang[k] = 0.0
        self.vx[k] = 0.0

        if r - l == 1:
            self.vy[k] = L[l]
        else:
            # 葉ではない節点
            chl = k * 2 + 1
            chr = k * 2 + 2
            self.create_node(chl, l, (l+r)//2)
            self.create_node(chr, (l+r)//2, r)
            self.vy[k] = self.vy[chl] + self.vy[chr]
    
    def change(self, k, a):
        """節点の更新

        Args:
            k (int): 節点の番号
            a (float): 変更分の角度（ラジアン）
        """
        
        def _change(k, a, v, l, r):
            # 更新する区間対象外なら何もしない
            if k <= l:
                return
            # 区間内
            elif k < r:
                chl = v * 2 + 1
                chr = v * 2 + 2
                m = (l + r) // 2
                _change(k, a, chl, l, m)
                _change(k, a, chr, m, r)

                # 中間よりも左側
                if k <= m:
                    self.ang[v] += a
                
                s = math.sin(self.ang[v])
                c = math.cos(self.ang[v])
                # vx[v]: 左ノードのx座標 + 右ノードのx座標
                self.vx[v] = self.vx[chl] + (c * self.vx[chr] - s * self.vy[chr])
                # vy[v]: 左ノードのx座標 + 右ノードのx座標
                self.vy[v] = self.vy[chl] + (s * self.vx[chr] + c * self.vy[chr])

        _change(k, a, 0, 0, self.n)


def solved():
    st = SegmentTree(N)

    # 初期値の角度は180度（ラジアン）
    prv = [math.pi]*N

    for i in range(C):
        s = S[i]
        a = A[i] / 360 * 2 * math.pi

        st.change(s, a-prv[s])
        prv[s] = a

        print(st.vx[0], st.vy[0])
    


if __name__ == '__main__':
    N, C = map(int, input().split())
    L = list(map(int, input().split()))
    S = list(map(int, input().split()))
    A = list(map(int, input().split()))

    solved()
