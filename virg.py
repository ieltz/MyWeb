import pandas as pd
import numpy

c = pd.read_csv('virginica.csv')

c.to_html('virginicaiel.html')

c_mean = c["SepalLengthCm"].mean()
c_median = c["SepalLengthCm"].median()
c_mode = c["SepalLengthCm"].mode()

c_mean1 = c["SepalWidthCm"].mean()
c_median1 = c["SepalWidthCm"].median()
c_mode1 = c["SepalWidthCm"].mode()

c_mean2 = c["PetalLengthCm"].mean()
c_median2 = c["PetalLengthCm"].median()
c_mode2 = c["PetalLengthCm"].mode()

c_mean3 = c["PetalWidthCm"].mean()
c_median3 = c["PetalWidthCm"].median()
c_mode3 = c["PetalWidthCm"].mode()

print(c.to_string())

print('\n"SepalLengthCm mean is:' + str(c_mean))
print('SepalLengthCm median is:' + str(c_median))
print('SepalLengthCm mode is:' + str(c_mode))

print('\n"SepalWidthCm mean is:' + str(c_mean1))
print('SepalWidthCm median is:' + str(c_median1))
print('SepalWidthCm mode is:' + str(c_mode1))

print('\n"PetaLengthCm mean is:' + str(c_mean2))
print('PetalLengthCm median is:' + str(c_median2))
print('PetalLengthCm mode is:' + str(c_mode2))

print('\n"PetalWidthCm mean is:' + str(c_mean3))
print('PetalWidthCm median is:' + str(c_median3))
print('PetalWidthCm mode is:' + str(c_mode3))
