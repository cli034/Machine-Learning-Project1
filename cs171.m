clc;clear;
a = load('test.mat');
bin = 5;
first = a.iris(:,1);
min_first = min(first);
max_first = max(first);
range = (max_first - min_first)/bin;
Y = zeros(1,bin);
r1 = min_first;
r2 = min_first + range;
X = cell(1,bin);
for i=1:bin
    X{i} = sprintf('%.1f-%.1f', r1, r2);
    Y(i) = size(first(first>r1 & first<=r2),1);
    r1 = r2;
    r2 = r2 + range;
end
X = categorical(X);
bar(X,Y);