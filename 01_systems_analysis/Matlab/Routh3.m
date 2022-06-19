clear, close; clc;

%% System
num = [15];
den = [1, 3, 3, 9, 4, 6];
close_sys = tf(num,den)

%% Stability (1= True, 0 = False)
isstable(close_sys)

%% Roots
pole(close_sys)

%% Diagram
pzmap(close_sys)