N = 1000000;

T = 0; %Tamper - independent
F = 0; %Fire - independent
A = 0; %Alarm - depends on T and F
S = 0; %Smoke - depends on F
L = 0; %Leaving - depends on A
R = 0; %Report - depends on L

PTamper = [0.02; 1-0.02]; PFire = [0.01;1-0.01];
PAlarm_g_Tamper_Fire = [0.5; 0.85; 0.99; 0.0001]; PAlarm_g_Tamper_Fire = [PAlarm_g_Tamper_Fire; 1 - PAlarm_g_Tamper_Fire];
PSmoke_g_Fire = [0.9; 0.01; 1-0.9; 1-0.01];
PLeaving_g_Alarm = [0.88; 0.001; 1-0.88; 1-0.001];
PReport_g_leaving = [0.75; 0.01; 1-0.75; 1-0.01];

%Say we want to find P(T | ~S and R)

samps = [];

for i = 1:N
    T=0; F=0; A=0; S=0; L=0; R=0;
    %T
    if(rand(1) < PTamper(1))
        T = 1;
    end
    %F
    if(rand(1) < PFire(1))
        F = 1;
    end
    %A
    if(T==1 && F==1 && rand(1) < PAlarm_g_Tamper_Fire(1))
        A = 1;
    elseif(T==1 && F==0 && rand(1) < PAlarm_g_Tamper_Fire(2))
        A = 1;
    elseif(T==0 && F==1 && rand(1) < PAlarm_g_Tamper_Fire(3))
        A = 1;
    elseif(T==0 && F==0 && rand(1) < PAlarm_g_Tamper_Fire(4))
        A = 1;
    end
    %S
    if(F==1 && rand(1) < PSmoke_g_Fire(1))
        S = 1;
    elseif(F==0 && rand(1) < PSmoke_g_Fire(2))
        S = 1;
    end
    %Reject sample if Smoke is true
    if(S==1)
        continue;
    end
    %L
    if(A==1 && rand(1) < PLeaving_g_Alarm(1))
        L = 1;
    elseif(A==0 && rand(1) < PLeaving_g_Alarm(2))
        L = 1;
    end
    %R
    if(L==1 && rand(1) < PReport_g_leaving(1))
        R = 1;
    elseif(L==0 && rand(1) < PReport_g_leaving(2))
        R = 1;
    end
    %Reject sample if Report is false
    if(R==0)
        continue;
    end
    %Update the list of non-rejected samples
    samps = [samps; T; F; A; S; L; R];
end

%Calculating the probability from the remaining samples
PTampers_given_nosmoke_Report = sum(samps(1:6:length(samps)) == 1)/(length(samps)/6);

disp(PTampers_given_nosmoke_Report)