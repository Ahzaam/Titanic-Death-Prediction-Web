import pickle
# import sklearn
from .models import Predictions

def model_prediction(x_data):
    model = pickle.load(open('titanic_model.sav','rb'))
    person = [[int(x_data.GET.get('gender')), int(x_data.GET.get('age')), int(x_data.GET.get('fare'))]]
    prediction = model.predict(person)

    Predictions.objects.create(age=person[0][1],gender=person[0][0],fare=person[0][2], pred=prediction[0])
    return prediction
