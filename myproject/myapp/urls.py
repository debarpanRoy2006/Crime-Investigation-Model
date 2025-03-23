from django.urls import path
from .views import home, login_view, signup_view, check_links, get_solutions, show_result, classify_crime
from .views import classify_crime_view  # ✅ Ensure this import is present
urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('prevent/', check_links, name='check_links'),
    path('index/', get_solutions, name='get_solutions'),
    path("classify/",classify_crime_view, name="classify_crime"),
    path("result/", show_result, name="result_page"),
]