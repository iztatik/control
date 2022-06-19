clear, close; clc;

% System
t_end = 10;
num = 38;
den = [1, 5, 6];
open_sys = tf(num,den)
close_sys = feedback(open_sys,1)

% Step response
amp = 10;
opt = stepDataOptions('StepAmplitude',amp);
step(close_sys,t_end, opt)
[y,t]=step(close_sys, t_end, opt);
step_error =abs(amp-y(end))
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


