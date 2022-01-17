function [result] = calculate(nums)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
% result = 2*(nums(1)^4);
% result = result + 3*(nums(2)^2);

% result = (1.5 - nums(1) + (nums(1)*nums(2)))^2;
% result = result + (2.25 - nums(1) + nums(1)*(nums(2))^2)^2
% result = result + (2.625 -nums(1) + nums(1) * (nums(2)^3))^2
% result = sqrt(2*nums(1)-5);
% result = 2*nums(1) - 5/nums(1);
% result = nums(1)^nums(2)+2*nums(1)^3+(nums(1)/nums(2));
% disp(size(nums));
% if nums(1) < 0
%     result = -2*(nums(2)^2)*(nums(3)^2)
% else
%     result = 3*(nums(2)^2+(nums(1)^2)*(nums(3)^2));
% end
result = sin(nums(1))+ (nums(2) * (1/cos(nums(3))));
end

