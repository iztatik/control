clear; close; clc;

% System
num = 25;
den = [1, 6, 25];
sys = tf(num,den)

% Step response and info
damp(sys)
stepinfo(sys)
step(sys)
grid on;
