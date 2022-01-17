% a = 10;
% b = 20;
% c = a+b;
% disp(c);

% d = [10,20,30,40];
% % e = [10,20,30,40];
% % f = d+e;
% % disp(f(1));
% 
% a = [10,20,30,40;
%     20,30,11,20;
%     15,25,15,22;
%     1,2,3,4;
%     5,10,15,20;
%     ];

% disp(a(:,1:3));
% disp(sum(a));
% disp(sum(sum(a)));
% 
% disp(size(a));
% disp(size(a,1));
% disp(size(a,2));
% s = 0
% for index=1:size(d)
%     s = s +d(index)
% end 
% disp(s);

% a = [10,20,30,40,50];
% b = [20,30,40,50,60];
% 
% s = 0;
% i = 1;
% limit = size(a,2);
% for i=1:limit
%     s=s+a(i);
% end
% length(a) => size(a,2)
% while i <= length(a)
%     s = s+a(i)^2;
%     i=i+1;
% end
% s = sqrt(s);
% disp(s);
% fprintf("%d is the summation\n",s); 
% k = "Oscar";
% fprintf("%s, your summation is %d.\n",k,s);
% result = (dotCalc(a,b))/(norm(a)*norm(b));
% t = tamimoto(a,b);

% fprintf("The norm, after called, is: %f",dot(a,b));
% 
% a=10;
% b=20;
% if a~=b
%     disp("Not Equal");
% else 
%     disp("Equal");

% A = [4,5,6,3;
%      1,1,2,4;
%      3,2,1,6;
%      5,7,9,8;]
%  
% sum = 0;
%  for x=1:size(A,1)
%      for y=1:size(A,2)
%          if x ~= y
%              sum = sum + A(x,y);
%          end
%      end
%  end
%              
% disp(sum);
% 
% sortrows(A)

% x = dlmread("untitled.txt", " ")
% disp(x)
% d
vector = [3,3];
matrix = [1,1;
          3.1,3.1;
          3.09,3.09];
number = 2;
disp(knn(vector,matrix,3)');
% fprintf("Similarity according to cosines, is: %f \n", t);