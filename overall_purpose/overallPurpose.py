from matplotlib import pyplot as plt
import readFromDatabase as rfd
import os

purpose_data = rfd.readAction('age_action', 'activity')
print(purpose_data)