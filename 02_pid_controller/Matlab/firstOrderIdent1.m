clear, close, clc;

% Open the .csv file and plot
data = readmatrix('data\delayedFirstOrder1.csv');

% Sorting data
t = data(:,1);
in = data(:,2);
out = data(:,3);

% Plot data
plot(t, in, t, out)
grid on;
pause()

% System estimation
data = iddata(out,in,0.05);
sys = procest(data, 'P1D')


