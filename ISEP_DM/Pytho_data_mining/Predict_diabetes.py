import os
os.chdir("/Users/tiagoreis/PycharmProjects/Python/ISEP_DM/Pytho_data_mining")
import timeit
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier as knnc
from sklearn.tree import DecisionTreeClassifier as dt
from sklearn.naive_bayes import GaussianNB as nb
from sklearn.svm import SVC as svm
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

# 1.Create a list of names (['NPG','PGC','DBP','TST','SIC','BMI','DPF','AGE','DIA']);
data_headers = ['NPG', 'PGC', 'DBP', 'TST', 'SIC', 'BMI', 'DPF', 'AGE', 'DIA']

# 2.Read ‘pima-indians-diabetes’ file data on python showing the column’s names:
data_diabetes = pd.read_csv("pima-indians-diabetes.csv", names=data_headers, index_col=None)
pd.DataFrame(data_diabetes)

# Remove rows where PGC, DBP and BMI equal 0
data = data_diabetes[(data_diabetes.PGC != 0) & (data_diabetes.DBP != 0) & (data_diabetes.BMI != 0)]

# Split the dataframe in train and test (80/20)
train, test = train_test_split(data, test_size=0.2)  # split in random sets

# Check the size of the subsets
print(train.shape)
print(test.shape)

# list the features (X)
features = ['NPG', 'PGC', 'DBP', 'TST', 'SIC', 'BMI', 'DPF', 'AGE']
# ...and the target (Y)
target = 'DIA'

# -------------------------------------------------------------------------------------------------------------------
# Measure the time it takes to train the models
starttime = timeit.default_timer()
# -------------------------------------------------------------------------------------------------------------------
# Let us measure the accuracy of KNN
score_knn = cross_val_score(knnc(), train[features], train[target])
# Print its accuracy
print('KNN mean accuracy: ', round(score_knn.mean()*100, 2), '% in', round(timeit.default_timer()-starttime, 3), 's.')

# Let us measure the accuracy of Decision Tree
score_dt = cross_val_score(dt(), train[features], train[target])
print('DTree mean accuracy: ', round(score_dt.mean()*100, 2), '% in', round(timeit.default_timer()-starttime, 3), 's.')

# Let us measure the accuracy of Naive Bayes
score_nb = cross_val_score(nb(), train[features], train[target])
print('GNBayes mean accuracy: ', round(score_nb.mean()*100, 2), '% in', round(timeit.default_timer()-starttime,3),'s.')

# Let us measure the accuracy of SVM
score_svm = cross_val_score(svm(kernel='linear'), train[features], train[target])
print('SVM mean accuracy: ', round(score_svm.mean()*100, 2), '% in', round(timeit.default_timer()-starttime, 3), 's.')

# -------------------------------------------------------------------------------------------------------------------
# It seems that GNB and SVM are the best! Let us train them

# Train GNBayes
model_nb = nb().fit(train[features], train[target])
# Test GNBayes
test_nb = model_nb.predict(test[features])
# Print its accuracy
print('GNB accuracy:', round(accuracy_score(test[target], test_nb)*100, 2), '%')

# Train SVM
model_svm = svm().fit(train[features], train[target])
# Test svm
test_svm = model_svm.predict(test[features])
# Print its accuracy
print('SVM accuracy:', round(accuracy_score(test[target], test_svm)*100, 2), '%')

# -------------------------------------------------------------------------------------------------------------------
# Let us compare their confusion Matrix
plt.title('GNB confusion matrix')
sns.heatmap(confusion_matrix(test[target], test_nb), annot=True)
plt.show()

plt.title('SVM confusion matrix')
sns.heatmap(confusion_matrix(test[target], test_svm), annot=True)
plt.show()
