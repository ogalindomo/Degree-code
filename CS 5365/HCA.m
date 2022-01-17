data = dlmread('datahac.txt', '	');
tree = linkage(data);
dendrogram(tree);
idx = cluster(tree, 'maxclust',3);