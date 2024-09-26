from django.shortcuts import render
from django.http import HttpResponse
from pickle import load 


# print(model)
def index(request):
    return render(request, 'index.html', {})

def aptitude(request):
    return render(request, 'aptitude.html', {})

def cgpa(request):
    return render(request, 'cgpa.html',{})

def result(request):
    file = open('ml-models/model.pkl', 'rb')
    model = load(file)
    file.close()
    cgpa = request.POST['cgpa']
    iq = request.POST['iq']
    prediction = model.predict([[float(cgpa), float(iq)]])
    print(prediction)
    if prediction[0] == 0:
        result = "Unfortunately there are less chances of your placement.All the best."
    else:
        result = "Congratulations you have a good chance of getting placement! :)"
    context = {"cgpa":cgpa, 'iq':iq, "result":result}
    return render(request, 'result.html', context)