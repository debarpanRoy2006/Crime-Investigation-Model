import json
import pickle
import os
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ml_model.train_model1 import classify_crime  
import os
import sys
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disable CSRF for testing (consider proper CSRF handling in production)
def classify_crime_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            description = data.get("description", "")

            # Process the description (Dummy response for testing)
            response_data = {"message": "Classification successful", "description": description}
            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)

# Ensure ml_model is in Python's module path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ml_model'))




# @csrf_exempt
# def classify_crime_view(request):
#     if request.method == 'POST':

#         return render(request, 'result.html', {
#             "category": "Cybercrime",
#             "section": "Section 66D",
#             "ipc": "IPC 420",
#             "punishment": "Imprisonment up to 3 years or fine up to Rs. 1 lakh or both",
#             "steps": "Report the incident to the nearest police station"
#         })

#         crime_description = request.POST.get("description", "")
#         if not crime_description:
#             return JsonResponse({"error": "No description provided"}, status=400)
        
#         result = classify_crime(crime_description)  # Call your ML function
        
#         return render(request, 'result.html', {
#             "category": result["Category"],
#             "section": result["Section"],
#             "ipc": result["IPC"],
#             "punishment": result["Punishment"],
#             "steps": result["Appropriate Steps"]
#         })
    
#     return JsonResponse({"error": "Only POST requests allowed"}, status=405)


# Load trained dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "ml_model/dataset/combined_data.sav")

with open(DATASET_PATH, "rb") as file:
    combined_df = pickle.load(file)

# Load TF-IDF model
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(combined_df["Processed_Desc"])

# Crime classification function
def classify_crime(description):
    processed_input = description.lower()
    input_vector = tfidf.transform([processed_input])
    similarities = cosine_similarity(input_vector, tfidf_matrix)
    best_match_idx = similarities.argmax()
    return combined_df.iloc[best_match_idx]

# API to handle crime classification


# Render the result.html page
def show_result(request):
    return render(request, "result.html")
