from math import sqrt
import random
class Solution1:
    def getMinDistSum(self, positions) -> float:
        eps = 1e-7
        alpha = 1.0
        decay = 1e-3

        n = len(positions)
        # 调整批大小
        batchSize = n

        x = sum(pos[0] for pos in positions) / n
        y = sum(pos[1] for pos in positions) / n

        # 计算服务中心 (xc, yc) 到客户的欧几里得距离之和
        getDist = lambda xc, yc: sum(((x - xc) ** 2 + (y - yc) ** 2) ** 0.5 for x, y in positions)

        while True:
            # 将数据随机打乱
            random.shuffle(positions)
            xPrev, yPrev = x, y

            for i in range(0, n, batchSize):
                j = min(i + batchSize, n)
                dx, dy = 0.0, 0.0

                # 计算导数，注意处理分母为零的情况
                for k in range(i, j):
                    pos = positions[k]
                    dx += (x - pos[0]) / (sqrt((x - pos[0]) * (x - pos[0]) + (y - pos[1]) * (y - pos[1])) + eps)
                    dy += (y - pos[1]) / (sqrt((x - pos[0]) * (x - pos[0]) + (y - pos[1]) * (y - pos[1])) + eps)

                x -= alpha * dx
                y -= alpha * dy

                # 每一轮迭代后，将学习率进行衰减
                alpha *= (1.0 - decay)

            # 判断是否结束迭代
            if ((x - xPrev) ** 2 + (y - yPrev) ** 2) ** 0.5 < eps:
                break

        return getDist(x, y)





class Solution:
    def getMinDistSum(self, positions) -> float:
        n = len(positions)
        def distance(x, y):
            d = 0
            for x_i, y_i in positions:
                d += ((x - x_i) ** 2 + (y - y_i) ** 2) ** 0.5
            return d
        x = sum(p[0] for p in positions) / n
        y = sum(p[1] for p in positions) / n
        lr = 0.2
        epsilon = 1e-7
        while True:
            d_x = d_y = 0
            x_pre, y_pre = x, y
            for x_i, y_i in positions:
                denominator = ((x - x_i) ** 2 + (y - y_i) ** 2) ** 0.5 + epsilon
                d_x += (x - x_i) / denominator
                d_y += (y - y_i) / denominator
            #x -= lr * (d_x / n)
            #y -= lr * (d_y / n)
            x -= lr * d_x
            y -= lr * d_y
            lr *= 0.999
            if abs(x - x_pre) < epsilon and abs(y - y_pre) < epsilon:
                break
        d = distance(x, y)
        return d

s = Solution()
positions = [[27,90],[99,75],[99,38]]
d = s.getMinDistSum(positions)
print(d)