clear, close, clc;

%% Data preprocesing
% Open the .csv file and plot
data = readmatrix('data\delayedFirtsOrder3.csv');

% Sorting data
t = data(:,1);
in = data(:,2);
out = data(:,3);

% Plot data
plot(t, in, t, out)
grid on;
pause()

%% System estimation
systemIdentification()
pause();
K = P1D.Kp;
T = P1D.Tp1;
L = P1D.Td;

%% PID

Kp = 1.2*T/(K*L);
Ti = 2*L;
Td = 0.5*L;

disp('PID: ')
fprintf('Kp = %1.4f \n', Kp);
fprintf('Ti = %1.4f, Ki = %1.4f \n', Ti, Kp/Ti);
fprintf('Td = %1.4f, Kd = %1.4f \n', Td, Kp*Td);

