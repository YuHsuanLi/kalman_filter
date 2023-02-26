# Kalman Filter
## Run
1. get ball moving gif
2. use opencv to detect the center of the ball
3. run main.py to see the difference between with and without kalman filter. And the effect of the process noise covariance and sensor noise covariance matrices. The larger the value in the sensor noise covariance matrix (R), the smoother the trajectory will be.
```
cd 2d
python video_generator.py
python detector.py
python main.py
``` 

## Result
![Alt text](2d/result.jpg?raw=true "Result")
