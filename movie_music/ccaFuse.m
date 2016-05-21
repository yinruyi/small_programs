function trainZ = ccaFuse(trainX, trainY, mode)

[n,p] = size(trainX);
if size(trainY,1) ~= n
    error('trainX and trainY must have the same number of samples.');
elseif n == 1
    error('trainX and trainY must have more than one sample.');
end
q = size(trainY,2);


if ~exist('mode', 'var')
    mode = 'sum';	% Default fusion mode
end


%% Center the variables

meanX = mean(trainX);
meanY = mean(trainY);
trainX = bsxfun(@minus, trainX, meanX);
trainY = bsxfun(@minus, trainY, meanY);


%% Dimensionality reduction using PCA for the first data X

% Calculate the covariance matrix
if n >= p
    C = trainX' * trainX;	% pxp
else
    C = trainX  * trainX';	% nxn
end

% Perform eigenvalue decomposition
[eigVecs, eigVals] = eig(C);
eigVals = abs(diag(eigVals));

% Ignore zero eigenvalues
maxEigVal = max(eigVals);
zeroEigIdx = find((eigVals/maxEigVal)<1e-6);
eigVals(zeroEigIdx) = [];
eigVecs(:,zeroEigIdx) = [];

% Sort in descending order
[~,index] = sort(eigVals,'descend');
eigVals = eigVals(index);
eigVecs = eigVecs(:,index);

% Obtain the projection matrix
if n >= p
    Wxpca = eigVecs;
else
    Wxpca = trainX' * eigVecs * diag(1 ./ sqrt(eigVals));
end
clear C eigVecs eigVals maxEigVal zeroEigIndex

% Update the first train data
trainX = trainX * Wxpca;


%% Dimensionality reduction using PCA for the second data Y

% Calculate the covariance matrix
if n >= q
    C = trainY' * trainY;	% qxq
else
    C = trainY  * trainY';	% nxn
end

% Perform eigenvalue decomposition
[eigVecs, eigVals] = eig(C);
eigVals = abs(diag(eigVals));

% Ignore zero eigenvalues
maxEigVal = max(eigVals);
zeroEigIndex = find((eigVals/maxEigVal)<1e-6);
eigVals(zeroEigIndex) = [];
eigVecs(:,zeroEigIndex) = [];

% Sort in descending order
[~,index] = sort(eigVals,'descend');
eigVals = eigVals(index);
eigVecs = eigVecs(:,index);

% Obtain the projection matrix
if n >= q
    Wypca = eigVecs;
else
    Wypca = trainY' * eigVecs * diag(1 ./ sqrt(eigVals));
end
clear C eigVecs eigVals maxEigVal zeroEigIndex

% Update the second train  data
trainY = trainY * Wypca;


%% Fusion using Canonical Correlation Analysis (CCA)

[Wxcca,Wycca] = canoncorr(trainX,trainY);

trainXcca = trainX * Wxcca;
trainYcca = trainY * Wycca;


if strcmp(mode, 'concat')	% Fusion by concatenation (Z1)
    trainZ = [trainXcca, trainYcca];
else                        % Fusion by summation (Z2)
    trainZ = trainXcca + trainYcca;
end