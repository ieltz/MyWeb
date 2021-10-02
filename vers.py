import pandas as pd
import numpy

b = pd.read_csv('versicolor.csv')

b.to_html('versicoloriel.html')

b_mean = b["SepalLengthCm"].mean()
b_median = b["SepalLengthCm"].median()
b_mode = b["SepalLengthCm"].mode()

b_mean1 = b["SepalWidthCm"].mean()
b_median1 = b["SepalWidthCm"].median()
b_mode1 = b["SepalWidthCm"].mode()

b_mean2 = b["PetalLengthCm"].mean()
b_median2 = b["PetalLengthCm"].median()
b_mode2 = b["PetalLengthCm"].mode()

b_mean3 = b["PetalWidthCm"].mean()
b_median3 = b["PetalWidthCm"].median()
b_mode3 = b["PetalWidthCm"].mode()

print(b.to_string())

print('\n"SepalLengthCm mean is:' + str(b_mean))
print('SepalLengthCm median is:' + str(b_median))
print('SepalLengthCm mode is:' + str(b_mode))

print('\n"SepalWidthCm mean is:' + str(b_mean1))
print('SepalWidthCm median is:' + str(b_median1))
print('SepalWidthCm mode is:' + str(b_mode1))

print('\n"PetaLengthCm mean is:' + str(b_mean2))
print('PetalLengthCm median is:' + str(b_median2))
print('PetalLengthCm mode is:' + str(b_mode2))

print('\n"PetalWidthCm mean is:' + str(b_mean3))
print('PetalWidthCm median is:' + str(b_median3))
print('PetalWidthCm mode is:' + str(b_mode3))
