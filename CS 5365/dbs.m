data = dlmread('dataDBS.txt', ',');
scatter(data(:,1),data(:,2));
idx = dbscan(data,1,10);
gscatter(data(:,1),data(:,2),idx);
