import predict
import utils

x_test = utils.getImages('./data/t10k-images-idx3-ubyte.gz', 100)
y_test = utils.getLabels('./data/t10k-labels-idx1-ubyte.gz', 100)
pred = predict.predictMLPClassifier(x_test[98])
print("Pred: "+str(pred)+", Actual: "+str(y_test[98]))