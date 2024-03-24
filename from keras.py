from keras.models import Sequential
from keras.layers import Input,ZeroPadding2D,Conv2D,BatchNormalization,Activation,MaxPool2D,Add,TimeDistributed
model=Sequential()
model.add(Input(shape=(None,None,3)))
model.add(ZeroPadding2D(padding=(2,2)))


model.add(Conv2D(filters=6,kernel_size=(16,16),strides=(2,2)))
model.add(BatchNormalization())
model.add(Activation())
model.add(MaxPool2D())

##############
model.add(Conv2D(filters=6,kernel_size=(16,16),strides=(2,2)))
model.add(BatchNormalization())
model.add(Activation())
###################

##############
model.add(Conv2D(filters=6,kernel_size=(16,16),strides=(2,2)))
model.add(BatchNormalization())
model.add(Activation())
###################


model.add(Conv2D(filters=6,kernel_size=(16,16),strides=(2,2)))
model.add(Conv2D(filters=6,kernel_size=(16,16),strides=(2,2)))

model.add(BatchNormalization())
model.add(BatchNormalization())

model.add(Add())



model.add(TimeDistributed())
model.add(TimeDistributed())

model.summary()