import readFromDatabase as rfd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

genderData=rfd.readCertainVisitor('visitor', 'gender', 'female')
carData=rfd.readCertainVisitor('visitor', 'cars', 'access to car (1+)')
marriedData=rfd.readCertainVisitor('visitor', 'married', 'married')
workingData=rfd.readCertainVisitor('visitor', 'working', 'employed/self-employed (full or part time)')