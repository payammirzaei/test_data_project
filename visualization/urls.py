from django.urls import path
from .views import dashboard, get_chart_data  # ✅ Make sure both are imported correctly
from visualization.views import dashboard,d3_dashboard, get_chart_data
urlpatterns = [
    path('', dashboard, name='dashboard'),  # Existing Plotly dashboard
    path('api/data/', get_chart_data, name='get_chart_data'),  # API for real-time data
    path('d3/', d3_dashboard, name='d3_dashboard'),  # New D3.js page
]

