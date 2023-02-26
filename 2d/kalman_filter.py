import numpy as np
from numpy.linalg import inv

class KalmanFilter():
    def __init__(self, RQratio):
        self.state = np.zeros(4) # x, y, vx, vy
        self.covariance = np.zeros(4)
        dt = 0.02
        self.A = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.C = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])
        self.std_weight_position = 1e-1 #1/100000
        self.std_weight_velocity = 1e-1 #1/250000
        self.RQratio = RQratio
        
    def init(self, measurement):
        self.state[0:2] = measurement
    
    def predict(self):
        state = self.A @ self.state
        std_Q = [
            self.std_weight_position,
            self.std_weight_position,
            self.std_weight_velocity,
            self.std_weight_velocity,
        ]
        covariance_Q = np.diag(np.square(std_Q))
        covariance = self.A @ self.covariance @ self.A.T + covariance_Q
        # self.state = state
        # self.covariance = covariance

        return state, covariance

    def correct(self, state, covariance, measurement):
        std_R = [
            self.RQratio*self.std_weight_position,
            self.RQratio*self.std_weight_position,
        ]
        covariance_R = np.diag(np.square(std_R))
        kalman_gain = covariance @ self.C.T @ inv(self.C@covariance@self.C.T+covariance_R)
        state = state + kalman_gain@(measurement[:2]-self.C@state)
        covariance = (np.eye(4)-kalman_gain@self.C)@covariance

        return state, covariance

    def update(self, measurement):
        state, covariance = self.predict()
        state, covariance = self.correct(state, covariance, measurement)
        self.state = state
        self.covariance = covariance
        x, y = self.state[0], self.state[1]
        return x, y


