function [knn_v] = knn(vector,matrix,neighbors_num)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
vector_similarities = zeros(size(matrix,1),2);
for i=1:size(matrix,1)
    d = distance(vector,matrix(i));
    vector_similarities(i,1) = i;
    vector_similarities(i,2) = d;
end
sorted = sortrows(vector_similarities,2);
knn_v = sorted(1:neighbors_num);
