clear, close; clc;

% System
num = 1;
den = [1, 7, 12, 0];
open_sys = tf(num,den)
close_sys = feedback(open_sys,1)

% Critical gain and period
[Kcr,Pm,Wcr,Wcp] = margin(open_sys);
Pcr = 2*pi/Wcr;
disp('Criticall gain:')
disp(Kcr)
disp('Criticall frequency(rad):')
disp(Wcr)
disp('Criticall period(seg):')
disp(Pcr);

% P controller
disp('P Controller:')
Kp_p = 0.5*Kcr;
fprintf('Kp: %2.4f\n\n', Kp_p)

% PI controller
disp('P Controller:')
Kp_pi = 0.45*Kcr;
Ti_pi = Pcr/1.2;
fprintf('Kp: %2.4f\n', Kp_pi)
fprintf('Ti: %2.4f\n\n', Ti_pi)

% PID controller
disp('PID Controller:')
Kp_pid = 0.6*Kcr;
Ti_pid = 0.5*Pcr;
Td_pid = 0.125*Pcr;
fprintf('Kp: %2.4f\n', Kp_pid)
fprintf('Ti: %2.4f\n', Ti_pid)
fprintf('Td: %2.4f\n\n', Td_pid)

% Rlocus
rlocus(open_sys)
grid on_
pause()

% Open block diagram
%open_system('PID\PID3.slx')
%sim('PID\PID3.slx',15)
