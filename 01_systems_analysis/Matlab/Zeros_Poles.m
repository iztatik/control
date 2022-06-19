clear; close; clc;

% TF definition
num = [1, 3];
den = [1, 2, -1, -2];
disp('Transfer fucntion')
sys = tf(num,den)

% Poles
P = pole(sys);
disp('Poles:')
disp(P)

% Zeros and gain
[Z, G] = zero(sys);
disp('Zeros:')
disp(Z)
disp('Gain:')
disp(G)

% Zeros and Poles diagram
pzmap(sys)
pause()

% Root locus
rlocus(sys)

