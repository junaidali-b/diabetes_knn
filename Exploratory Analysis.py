from matplotlib import pyplot as plt
import numpy as np
import pickle
#Loading variables from Pickle backup

pickle.load("diabetes.pkl")


#Visualising Diabetes positives and negatives by sex

outcome_true = len(raw_data.query('Outcome == 1'))
outcome_false = len(raw_data.query('Outcome == 0'))
imbalance = max(outcome_true, outcome_false) - min(outcome_true, outcome_false)
pie_count = np.array([outcome_true, outcome_false])
pie_labels = ['Diabetic', 'Non-Diabetic']
pie_colours = ['red', 'green']

plt.pie(pie_count, 
        labels= pie_labels, 
        colors=pie_colours, 
        autopct='%1.1f%%')

plt.title('Diabetic V/S Non- Diabetic Women',
          fontdict={'fontsize': 14, 
                    'fontweight': 'bold', 
                    'horizontalalignment': 'center'})
plt.show()
