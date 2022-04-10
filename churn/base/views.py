from django.shortcuts import render

# Create your views here.
import pickle

def home(request):
    return render(request, 'index.html')

def getPredictions(Age,BusinessTravel,DailyRate,Department,DistanceFromHome,Education, EducationField, EnvironmentSatisfaction, Gender,HourlyRate,
                        JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus, MonthlyIncome, MonthlyRate,NumCompaniesWorked, OverTime,  PercentSalaryHike,
                        PerformanceRating, RelationshipSatisfaction,StockOptionLevel,TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance,YearsAtCompany, 
                        YearsInCurrentRole, YearsSinceLastPromotion,YearsWithCurrManager):
    model = pickle.load(open('adbmodel', 'rb'))
    # scaled = pickle.load(open('scaler.sav', 'rb'))

    prediction = model.predict([[Age,BusinessTravel,DailyRate,Department,DistanceFromHome,Education, EducationField, EnvironmentSatisfaction, Gender,HourlyRate,
                        JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus, MonthlyIncome, MonthlyRate,NumCompaniesWorked, OverTime,  PercentSalaryHike,
                        PerformanceRating, RelationshipSatisfaction,StockOptionLevel,TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance,YearsAtCompany, 
                        YearsInCurrentRole, YearsSinceLastPromotion,YearsWithCurrManager]])
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'

def result(request):
    Age=int(request.GET['Age'])
    BusinessTravel=int(request.GET['BusinessTravel'])
    DailyRate=int(request.GET['DailyRate'])
    Department=int(request.GET['Department'])
    DistanceFromHome=int(request.GET['DistanceFromHome'])
    Education=int(request.GET['Education'])
    EducationField=int(request.GET['EducationField']) 
    EnvironmentSatisfaction=int(request.GET['EnvironmentSatisfaction'])
    Gender=int(request.GET['Gender'])
    HourlyRate=int(request.GET['HourlyRate'])
    JobInvolvement=int(request.GET['JobInvolvement'])
    JobLevel=int(request.GET['JobLevel'])
    JobRole=int(request.GET['JobRole'])
    JobSatisfaction=int(request.GET['JobSatisfaction'])
    MaritalStatus=int(request.GET['MaritalStatus'])
    MonthlyIncome=int(request.GET['MonthlyIncome'])
    MonthlyRate=int(request.GET['MonthlyRate'])
    NumCompaniesWorked=int(request.GET['NumCompaniesWorked'])
    OverTime=int(request.GET['OverTime']) 
    PercentSalaryHike=int(request.GET['PercentSalaryHike'])
    PerformanceRating=int(request.GET['PerformanceRating']) 
    RelationshipSatisfaction=int(request.GET['RelationshipSatisfaction'])
    StockOptionLevel=int(request.GET['StockOptionLevel'])
    TotalWorkingYears=int(request.GET['TotalWorkingYears'])
    TrainingTimesLastYear=int(request.GET['TrainingTimesLastYear'])
    WorkLifeBalance=int(request.GET['WorkLifeBalance'])
    YearsAtCompany=int(request.GET['YearsAtCompany']) 
    YearsInCurrentRole=int(request.GET['YearsInCurrentRole'])
    YearsSinceLastPromotion=int(request.GET['YearsSinceLastPromotion'])
    YearsWithCurrManager=int(request.GET['YearsWithCurrManager'])

    result = getPredictions(Age,BusinessTravel,DailyRate,Department,DistanceFromHome,Education, EducationField, EnvironmentSatisfaction, Gender,HourlyRate,
                        JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus, MonthlyIncome, MonthlyRate,NumCompaniesWorked, OverTime,  PercentSalaryHike,
                        PerformanceRating, RelationshipSatisfaction,StockOptionLevel,TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance,YearsAtCompany, 
                        YearsInCurrentRole, YearsSinceLastPromotion,YearsWithCurrManager)

    return render(request, 'result.html', {'result': result})


