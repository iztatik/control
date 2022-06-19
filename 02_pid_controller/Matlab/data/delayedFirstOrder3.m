clear; close; clc;

% Step parameters
stp_amp = 1; 
stp_time = 50;      % Seconds
smpl_time = 0.05;   % Seconds

% Delayed first-order parameters
k = 1.25;          % System gain
T = 5.18;          % Time constant
L = 2.14;          % Delay 

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
writematrix([t,u,y], 'delayedFirtsOrder3.csv')