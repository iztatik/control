clear; close; clc;

% Step parameters
stp_amp = 3; 
stp_time = 15;      % Seconds
smpl_time = 0.01;   % Seconds

% Delayed first-order parameters
k = 0.8;          % System gain
T = 0.4;          % Time constant
L = 0.7;          % Delay 

% Transfer function definition
num = k;
den = [T 1];
sys_op = tf(num,den,'InputDelay',L)

% Step response
t= (0:smpl_time:stp_time)';
u = stp_amp*ones(size(t));
y = step(stp_amp*sys_op,t);

% Adding noise
noise = 0.04*k*randn(size(y));
y = y + noise;

% Plot 
plot(t, u, t, y);
grid on;

% Export to .csv
writematrix([t,u,y], 'delayedFirtsOrder2.csv')