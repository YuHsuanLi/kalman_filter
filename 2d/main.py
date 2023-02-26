import numpy as np
import matplotlib.pyplot as plt
from kalman_filter import KalmanFilter

# without KF
center = np.load('center.npy')
RQratios = [0.2, 0.5, 1, 2, 5]

plt.figure(figsize=(12, 8))
plt.subplot(231)
plt.plot(center[:, 0], center[:, 1], label='w/o kf', color='C0')
plt.legend(loc='upper center')

# with KF
for i, RQratio in enumerate(RQratios):
	center_kf_list = []
	kf = KalmanFilter(RQratio)
	kf.init(center[0])
	for measurement in center[1:]:
		x, y = kf.update(measurement)
		center_kf_list.append([x, y])
	center_kf_list = np.array(center_kf_list)
	plt.subplot(230+i+2)
	plt.plot(center_kf_list[:, 0], center_kf_list[:, 1], label='w/ kf, RQratio= ' + str(RQratio), color='C'+str(i+1))
	plt.legend(loc='upper center')
plt.savefig('result.png')
plt.show()	