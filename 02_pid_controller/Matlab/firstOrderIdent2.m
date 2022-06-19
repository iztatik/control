clear, close, clc;

% Open the .csv file and plot
data = readmatrix('data\delayedFirtsOrder2.csv');

% Sorting data
t = data(:,1);
in = data(:,2);
out = data(:,3);

% Plot data
plot(t, in, t, out)
grid on;
pause()

% Sistem estimation
systemIdentification()
