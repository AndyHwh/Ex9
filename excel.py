import xlrd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

def linear_model_main(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

# Function to show the resutls of linear fit model
def show_linear_line(X_parameters, Y_parameters1,Y_parameters2):
    regr1 = linear_model.LinearRegression()
    regr2 = linear_model.LinearRegression()
    regr1.fit(X_parameters, Y_parameters1)
    regr2.fit(X_parameters, Y_parameters2)
    plt.scatter(X_parameters, Y_parameters1, color='blue')
    plt.scatter(X_parameters, Y_parameters2, color='blue')
    plt.plot(X_parameters, regr1.predict(X_parameters), color='red', linewidth=2)
    plt.plot(X_parameters, regr2.predict(X_parameters), color='red', linewidth=2)
    plt.xticks(())
    plt.yticks(())
    plt.show()

f=xlrd.open_workbook("/users/wangfeng/Desktop/price.xlsx")
sheet=f.sheets()[0]
f1= np.array(sheet.col_values(1)[1:5])
f2=np.array(sheet.col_values(2)[1:5])
x=(np.arange(1,len(f1)+1)).reshape(-1,1)
print(linear_model_main(x,f1,0))
print(linear_model_main(x,f2,0))
show_linear_line(x,f1,f2)


# plt.figure(figsize=(16,4))
# plt.plot(x,f1,color='red',label="min",linewidth=2)
# plt.plot(x,f2,color='blue',label="ave",linewidth=2)
# plt.xlabel("month")
# plt.ylabel("price")
# plt.ylim(min(f1)-1000,max(f2)+1000)
# plt.legend()
# plt.show()