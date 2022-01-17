% display(calculate([1,1]));
options = optimset('Display','iter','MaxFunEvals',120000,'TolFun',1.0e-20,'MaxIter',400);
x = [0,0,0];
disp(calculate(x));
[xx,fval] = fminunc(@calculate,x,options);
disp(xx);