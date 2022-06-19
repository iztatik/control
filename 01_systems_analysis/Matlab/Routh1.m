clear, close; clc;

% System
num = 25;
den = [1, 6, 0];
open_sys = tf(num,den)
close_sys = feedback(open_sys,1)

% Stability (1= True, 0 = False)
isstable(close_sys)

% Roots
pole(close_sys)
