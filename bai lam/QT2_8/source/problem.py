import numpy as np
import matplotlib.pyplot as plt
import cv2
import random


class Problem:
    def __init__(self, filename):
        self.X, self.Y, self.Z = self.load_state_space(filename)
    
    def load_state_space(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        h, w = img.shape
        X = np.arange(w)
        Y = np.arange(h)
        Z = img
        return X, Y, Z
    
    def show(self):
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        fig = plt.figure(figsize=(8,6))
        ax = plt.axes(projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.plot(range(0, 50), range(0, 50), self.Z[range(0, 50), range(0, 50)], 'r-', zorder=3, linewidth=0.5)
        plt.show()

    def draw_path(self, path):
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        fig = plt.figure(figsize=(8,6))
        ax = plt.axes(projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        # Vẽ điểm từ path
        path_array = np.array(path)  # Chuyển list path thành mảng numpy để dễ xử lý
        ax.plot(path_array[:, 0], path_array[:, 1], path_array[:, 2], 'r-', zorder=3, linewidth=0.5)
        plt.show()

    def get_random_state(self):
        # Tạo một trạng thái ngẫu nhiên trong không gian trạng thái
        x = random.randint(0, len(self.X) - 1)  # Chọn ngẫu nhiên một giá trị x
        y = random.randint(0, len(self.Y) - 1)  # Chọn ngẫu nhiên một giá trị y
        z = self.Z[y, x]  # Lấy giá trị z tương ứng với vị trí (x, y)
        return x, y, z
    
    def evaluate_state(self, current_state):
        return current_state[-1]
    
    def get_the_best_neighbor(self, current_state):
        x,y,z = current_state
        current_evaluate = z
        the_best_neighbor = None

        # Lặp qua các hướng xung quanh trạng thái hiện tại (trên mặt phẳng)
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for k in range(8):
            # Tính toán tọa độ mới của trạng thái láng giềng
            new_x = x + dx[k]
            new_y = y + dy[k]

            # Kiểm tra xem trạng thái mới có nằm trong phạm vi không gian trạng thái hay không
            if 0 <= new_x < len(self.X) and 0 <= new_y < len(self.Y):
                new_z = self.Z[new_y, new_x]
                # So sánh tìm hàng xóm có evaluate tốt nhất
                if  new_z > current_evaluate:
                    current_evaluate = new_z
                    the_best_neighbor = (new_x, new_y, new_z)
        return the_best_neighbor

    def initial_state(self):
        state = self.get_random_state()
        state_value = state[2]
        return state, state_value
    
    def random_neighbor(self,current_state):
        x,y,z = current_state
        neighbors_valid_stateSpace = []
        # tọa độ các đỉnh kề với current_state
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        # lặp qua các đỉnh kề
        for k in range(8):
            new_x = x + dx[k]
            new_y = y + dy[k]

            # Kiểm tra xem trạng thái mới có nằm trong phạm vi không gian trạng thái hay không
            if 0 <= new_x < len(self.X) and 0 <= new_y < len(self.Y):
                new_z = self.Z[new_y, new_x]
                neighbors_valid_stateSpace.append((new_x,new_y,new_z))

        neighbor_valid = random.choice(neighbors_valid_stateSpace)
        neighbor_value = neighbor_valid[2]

        return neighbor_valid, neighbor_value
    
    def get_k_randomly_state(self,k):
        x_domain = range(len(self.X))
        y_domain = range(len(self.Y))
        k_x = random.sample(x_domain,k)
        k_y = random.sample(y_domain,k)
        k_state = []
        for i in range(k):
            x = k_x[i]
            y = k_y[i]
            z = self.Z[y,x]
            k_state.append((x,y,z))
        return k_state

    def neighbors(self, current_state):
        x,y,z = current_state
        neighbors_valid_stateSpace = []
        # tọa độ các đỉnh kề với current_state
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for k in range(8):
            new_x = x + dx[k]
            new_y = y + dy[k]

            # Kiểm tra xem trạng thái mới có nằm trong phạm vi không gian trạng thái hay không
            if 0 <= new_x < len(self.X) and 0 <= new_y < len(self.Y):
                new_z = self.Z[new_y, new_x]
                neighbors_valid_stateSpace.append((new_x,new_y,new_z))

        return neighbors_valid_stateSpace
    
        
