from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib  # Assuming you are using joblib to load your ML model

# Load your ML model (adjust the path to your model file)
model = joblib.load('path/to/your/model.pkl')

@csrf_exempt
def classify(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            description = data.get('description', '')

            # Perform classification using the ML model
            prediction = model.predict([description])[0]

            # Create a response dictionary
            response = {
                'Category': prediction['category'],
                'Section': prediction['section'],
                'IPC': prediction['ipc'],
                'Punishment': prediction['punishment'],
                'Steps_to_Take': prediction['steps_to_take']
            }

            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
