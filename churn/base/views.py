from django.shortcuts import render

# Create your views here.
import pickle

from requests import request

def home(request):
    return render(request, 'index.html')

def getPredictions(OverTime,DistanceFromHome,Age,EnvironmentSatisfaction,TotalWorkingYears,MonthlyIncome,YearsAtCompany,JobRole,JobInvolvement,WorkLifeBalance,JobLevel,
    YearsInCurrentRole,DailyRate,MaritalStatus,JobSatisfaction,TrainingTimesLastYear,YearsSinceLastPromotion,MonthlyRate,StockOptionLevel,YearsWithCurrManager):
    model = pickle.load(open('gnbmodel2', 'rb'))
    
    prediction = model.predict([[OverTime,DistanceFromHome,Age,EnvironmentSatisfaction,TotalWorkingYears,MonthlyIncome,YearsAtCompany,JobRole,JobInvolvement,WorkLifeBalance,JobLevel,
    YearsInCurrentRole,DailyRate,MaritalStatus,JobSatisfaction,TrainingTimesLastYear,YearsSinceLastPromotion,MonthlyRate,StockOptionLevel,YearsWithCurrManager]])
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'

def result(request):
    OverTime=int(request.GET['OverTime'])
    DistanceFromHome=int(request.GET['DistanceFromHome'])
    Age=int(request.GET['Age'])
    EnvironmentSatisfaction=int(request.GET['EnvironmentSatisfaction'])
    TotalWorkingYears=int(request.GET['TotalWorkingYears'])
    MonthlyIncome=int(request.GET['MonthlyIncome'])
    YearsAtCompany=int(request.GET['YearsAtCompany'])
    JobRole=int(request.GET['JobRole'])
    JobInvolvement=int(request.GET['JobInvolvement'])
    WorkLifeBalance=int(request.GET['WorkLifeBalance'])
    JobLevel=int(request.GET['JobLevel'])
    YearsInCurrentRole=int(request.GET['YearsInCurrentRole'])
    DailyRate=int(request.GET['DailyRate'])
    MaritalStatus=int(request.GET['MaritalStatus'])
    JobSatisfaction=int(request.GET['JobSatisfaction'])
    TrainingTimesLastYear=int(request.GET['TrainingTimesLastYear'])
    YearsSinceLastPromotion=int(request.GET['YearsSinceLastPromotion'])
    MonthlyRate=int(request.GET['MonthlyRate'])
    StockOptionLevel=int(request.GET['StockOptionLevel'])
    YearsWithCurrManager=int(request.GET['YearsWithCurrManager'])

    result = getPredictions(OverTime,DistanceFromHome,Age,EnvironmentSatisfaction,TotalWorkingYears,MonthlyIncome,YearsAtCompany,JobRole,JobInvolvement,WorkLifeBalance,JobLevel,
YearsInCurrentRole,DailyRate,MaritalStatus,JobSatisfaction,TrainingTimesLastYear,YearsSinceLastPromotion,MonthlyRate,StockOptionLevel,YearsWithCurrManager)

    return render(request, 'result.html', {'result': result})




