clear; close; clc;

%% System 
num = [40];
den = [1, 2, 0];
disp('System transfer functions:')
op_sys = tf(num,den)
cl_sys = feedback(op_sys,1)

%% Compensators
% Compensated system response(Mp=20.5)
Gc1 = tf(2.45127*[1,4],[1,10.4818])
opCom_sys1=tf(Gc1*op_sys);
clCom_sys1=feedback(opCom_sys1,1);

% Compensated system response (z=0.76)
Gc2 = tf(2.9380*[1,4],[1,22.97])
opCom_sys2=tf(Gc2*op_sys);
clCom_sys2=feedback(opCom_sys2,1);

% Compensated system response (z=0.76, annulation)
Gc3 = tf(0.6925*[1,2],[1,8])
opCom_sys3=tf(Gc3*op_sys);
clCom_sys3=feedback(opCom_sys3,1);


%% Specifications
% Non-compensated specitications
disp('Non-compensated specifications:')
stepinfo(cl_sys)

% Compensated specitications(Mp=20.5) 
disp('Compensated specifications (Mp=20.5):')
stepinfo(clCom_sys1)

% Compensated specitications(z=0.76) 
disp('Compensated specifications(z=0.76):')
stepinfo(clCom_sys2)

% Compensated specitications(annulation) 
disp('Compensated specifications(annulation):')
stepinfo(clCom_sys3)

%% Step response 
% Non-compensated system step response
figure
step(cl_sys)
grid on;
hold on;

% Compensated response (Mp=20.5)
step(clCom_sys1)

% Compensated response (z=0.76)
step(clCom_sys2)

% Compensated response (annulation)
step(clCom_sys3)

legend('Non-compensated','Compensated','Compensated z=0.76', 'Compensated(annulation)')
%% Root locus
%Root locus
figure
title('Uncompensated')
rlocus(op_sys)
figure
title('Compensated')
rlocus(opCom_sys1)
