import pandas as pd
import numpy

a = pd.read_csv('setosa.csv')

a.to_html('setosaiel.html')

a_mean = a["SepalLengthCm"].mean()
a_median = a["SepalLengthCm"].median()
a_mode = a["SepalLengthCm"].mode()

a_mean1 = a["SepalWidthCm"].mean()
a_median1 = a["SepalWidthCm"].median()
a_mode1 = a["SepalWidthCm"].mode()

a_mean2 = a["PetalLengthCm"].mean()
a_median2 = a["PetalLengthCm"].median()
a_mode2 = a["PetalLengthCm"].mode()

a_mean3 = a["PetalWidthCm"].mean()
a_median3 = a["PetalWidthCm"].median()
a_mode3 = a["PetalWidthCm"].mode()

print(a.to_string())

print('\n"SepalLengthCm mean is:' + str(a_mean))
print('SepalLengthCm median is:' + str(a_median))
print('SepalLengthCm mode is:' + str(a_mode))


print('\n"SepalWidthCm mean is:' + str(a_mean1))
print('SepalWidthCm median is:' + str(a_median1))
print('SepalWidthCm mode is:' + str(a_mode1))

print('\n"PetaLengthCm mean is:' + str(a_mean2))
print('PetalLengthCm median is:' + str(a_median2))
print('PetalLengthCm mode is:' + str(a_mode2))

print('\n"PetalWidthCm mean is:' + str(a_mean3))
print('PetalWidthCm median is:' + str(a_median3))
print('PetalWidthCm mode is:' + str(a_mode3))
