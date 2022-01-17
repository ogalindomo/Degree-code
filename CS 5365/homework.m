data = dlmread('datum.txt', '	');
benchmark = dlmread('expectedclusters.txt');
[assignments,C,sumd] = kmeans(data,3);
a = (avgDistances(data,assignments));
disp(a);
disp(sumd);
b = sum(sumd);
sprintf('%5.f',sum(sumd)/3)
% max = 0;
% max_idx = 0;
% for iter = 1:10000
%     assignments = kmeans(data,3);
%     score = randAlgorithm(assignments,benchmark);
%     if score > max
%         max_idx = assignments;
%         max = score;
%     end
% end
% disp(max);

% tree = linkage(data);
% dendrogram(tree);
% idx = cluster(tree, 'maxclust',3);
% score = randAlgorithm(idx,benchmark);
% disp(score);
% assignments = kmeans(data,3);
% s = silhouette(data,assignments,'sqeuclid');
% disp(s);
% average = 0;
% for i = 1:size(s)
%     average = average + s(i);
% end
% disp(average);
% disp(average/size(s,1));
% max = 0;
% max_idx=0;
% for iter = 1:10000
%     idx = cluster(tree, 'maxclust',3);
%     score = randAlgorithm(idx,benchmark);
%     if score > max
%         max = score;
%         max_idx = idx;
%     end
% end 
% disp(max);
% a = (avgDistances(data,assignments));
% sprintf('%5.f',a)
