import numpy
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
numpy.random.seed(7)
dataset = numpy.genfromtxt("cs-training.csv",delimiter=',',skip_header =1)
X = dataset[:700,2:10]
Y = dataset[:700,1]
ex = dataset[701:1400,2:10]
ey = dataset[701:1400,1]
model = Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(7,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=200,batch_size=10)
result = model.evaluate(ex,ey)
print("\n%s : %.2f%%"%(model.metrics_names[1],result[1]*100))
prediction = model.predict(X)
rounded = (round(x[0] for x in prediction))
print(rounded)
