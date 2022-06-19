clear, close; clc;

% System
t_end = 10;
num = 25;
den = [1, 6, 0];
open_sys = tf(num,den)
close_sys = feedback(open_sys,1)

% Step response
step(close_sys,t_end)
[y,t]=step(close_sys, t_end );
step_error =abs(1-y(end))
grid on
pause()

% Ramp response
ramp=t;
[y,t]=lsim(close_sys ,ramp,t);
plot(t,y,t,ramp)
ramp_error =abs(ramp(end)-y(end))
grid on
pause()

% Parabolic response
parabolic=t.^2;
[y,t]=lsim(close_sys ,parabolic,t);
plot(t,y,t,parabolic)
grid on
parabolic_error =abs(ramp(end)-y(end))


