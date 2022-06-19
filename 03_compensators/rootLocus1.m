clear; close; clc;

%% Open-loop transfer function 
num = [1 2];
den = [1 4 13];
o_sys = tf(num,den)

%% Root-Locus
rlocus(o_sys)

%% Closed-loop transfer fucntion
c_sys = feedback(o_sys,1)
disp('Closed loop transfer fucntion:');

%% Poles
disp('Open-loop poles:')
pole(o_sys)

disp('Closed-loop poles:')
pole(c_sys)