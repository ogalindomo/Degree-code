function [average] = avgDistances(data,assignments)

centroids = zeros(3,13);
count = zeros(3,1);
distances = zeros(3,1);

for i = 1:size(data,1) %Sums the vectors of every datapoint to an entry in a matrix called "sums".
    count(assignments(i)) = count(assignments(i)) + 1; %Update number of data points.
    centroids(assignments(i),:) = centroids(assignments(i),:) + data(i,:); %Add the vector.
end
centroids(:,:) = centroids(:,:)./count(:);%Divides every entry of the summation by the size of the cluster.

for i = 1:size(data,1)
    distances(assignments(i),1) = distances(assignments(i),1) + sqrt(sum((centroids(assignments(i),:) - data(i,:)).^2));
end

total_sums = sum(distances);
average = total_sums/3;
end



