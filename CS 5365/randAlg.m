data = dlmread('data.txt', '	');
expected = dlmread('expected.txt');

max = 0;
for iter=1:100000
    calculated = (kmeans(data,3));
    TP = 0;
    FP = 0;
    TN = 0;
    FN = 0;

    for firstElemen = 1:size(expected,1)-1
        for secondElemen = firstElemen+1:size(expected,1)
            if calculated(firstElemen) == calculated(secondElemen)
                if expected(firstElemen) == expected(secondElemen)
                    TP = TP + 1;
                else
                    FP = FP + 1;
                end
            else
                if expected(firstElemen) == expected(secondElemen)
                    FN = FN + 1;
                else
                    TN = TN + 1;
                end
            end
        end
    end
    end_result = (TP+TN)/(TP+TN+FP+FN);
    if end_result > max
        max = end_result;
    end
end

disp(max);