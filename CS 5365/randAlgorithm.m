function [analysisScore] = randAlgorithm(calculated,benchmark)
analysisScore = 0;
TP = 0;
FP = 0;
TN = 0;
FN = 0;

for firstElemen = 1:size(benchmark,1)-1
    for secondElemen = firstElemen+1:size(benchmark,1)
        if calculated(firstElemen) == calculated(secondElemen)
            if benchmark(firstElemen) == benchmark(secondElemen)
                TP = TP + 1;
            else
                FP = FP + 1;
            end
        else
            if benchmark(firstElemen) == benchmark(secondElemen)
                FN = FN + 1;
            else
                TN = TN + 1;
            end
        end
    end
end
end_result = (TP+TN)/(TP+TN+FP+FN);
if end_result > analysisScore
    analysisScore = end_result;
end    
end


