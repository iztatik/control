clear; close; clc;

% TF definition
p = input('Introduzca el coeficiente del polo: ');
num = 6*[1, p];
den = [1, 5, 6];
disp('Transfer fucntion')
sys = tf(6,den);            % System without pole
sys_Pole = tf(num,den)      % System with single pole
diff_sys= tf([6, 0],den);   % Derivate of the system without pole 

% Respuesta al escalón
step(sys)
hold on;
step(sys_Pole)
step(diff_sys)
legend('No Pole','With Pole','No Pole derivative')
grid on;

