import gzip
import numpy as np

def getImages(fileName, count):
    f = gzip.open(fileName, 'r')
    image_size = 28
    
    f.read(16)
    buf = f.read(count * image_size * image_size) # read count
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    data = data.reshape(count, image_size, image_size, 1) # reshape to a multi-dim array
    f.close()

    images = list()
    for i in range(0, count):
        image = np.asarray(data[i]).squeeze()
        images.append(image.flatten())

    return images


def getLabels(fileName, count):
    f = gzip.open(fileName, 'r')
    label_size = 1
    f.read(8)
    buf = f.read(label_size * count)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int32)
    f.close()
    return labels
