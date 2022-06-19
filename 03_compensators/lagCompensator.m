clear; close; clc;

%% Simulation parameters
t_end = 200;

%% System 
num = [164.6];
den = [1,13,32,20];
disp('System transfer functions:')
opSys = tf(num,den)
clSys = feedback(opSys,1)
disp('Non-compensated poles:')
disp(pole(clSys))

%% Non-compensated steady state error
[y,t]=step(clSys, t_end);
step_error =abs(1-y(end));
disp('Non-compensated steady state error:')
disp(step_error)

%% Lag compensator
kc = 0.927
Gc=tf([1, 1/5],[1, 0.018028])

%% Compensated poles and steady state error
opCompSys = Gc*opSys;
clCompSys = feedback(opCompSys,1);
[y2,t2]=step(clCompSys, t_end);
step_error =abs(1-y2(end));
disp('Compensated poles:')
disp(pole(clCompSys))
disp('Compensated steady state error:')
disp(step_error)

%% Root locus
figure
rlocus(opSys)
grid on
title('Non-compensated')
pause 
close all
rlocus(opCompSys)
title('Compensated')
grid on
pause
close all
rlocus(kc*opCompSys)
title('Compensated with gain')
grid on
pause

%% Step response
% Non-compensated
figure
step(clSys);
grid on
hold on
% Compensated
step(clCompSys);
% Compensated with gain
step(feedback(kc*opCompSys,1));
legend('Non-compensated','Compensated', 'Compensated with gain')
