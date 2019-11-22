import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplot
import gzip
import struct
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
import utils

train_size = 60000
test_size = 10000

x_train = utils.getImages('./data/train-images-idx3-ubyte.gz', train_size)
#print(len(x))
#print(x[1].shape)
#image = np.reshape(x[2], (28,28))
#plt.imshow(image, cmap='gray', vmin=0, vmax=255)
#plt.show()
y_train = utils.getLabels("./data/train-labels-idx1-ubyte.gz", train_size)

#### Build the model
mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', alpha=1e-4,
                    solver='sgd', tol=1e-4, random_state=1,
                    learning_rate_init=.1, verbose=True)

mlp.fit(x_train, y_train)

x_test = utils.getImages('./data/t10k-images-idx3-ubyte.gz', test_size)
y_test = utils.getLabels('./data/t10k-labels-idx1-ubyte.gz', train_size)
predictions = mlp.predict(x_test)
print("Predictions")
print(predictions[:50])
print("True values")
print(y_test[:50])
print(accuracy_score(y_test, predictions))

# save the model
joblib.dump(mlp, "classifModel")