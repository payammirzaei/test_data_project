import requests
import plotly.graph_objects as go
from django.http import JsonResponse
from django.shortcuts import render

# Function to fetch real-time test data
def fetch_test_data():
    url = "https://random-data-api.com/api/vehicle/random_vehicle"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# ✅ Main Dashboard Page
def dashboard(request):
    return render(request, 'visualization/dashboard.html')

# ✅ API Function to Return Updated Chart Data (with Stored History)
def get_chart_data(request):
    # Load previous data from session
    if "test_data" not in request.session:
        request.session["test_data"] = []

    historical_data = request.session["test_data"]  # Get stored records

    # Fetch new records
    new_data = [fetch_test_data() for _ in range(5)]  # Fetch 5 new test samples

    # Filter out invalid records
    valid_data = [item for item in new_data if item and 'doors' in item and 'mileage' in item and 'kilometrage' in item]
    
    # Append new data to history
    historical_data.extend(valid_data)

    # Limit to the last 50 records to prevent infinite growth
    request.session["test_data"] = historical_data[-50:]
    request.session.modified = True  # Mark session as updated

    # Extract data for visualization
    x_values = list(range(len(historical_data)))  # Time index
    doors_values = [item["doors"] for item in historical_data]
    mileage_values = [item["mileage"] for item in historical_data]
    kilometrage_values = [item["kilometrage"] for item in historical_data]

    # Create graph data
    chart_data = {
        "line_chart": {
            "x": x_values,
            "y": mileage_values,
            "type": "scatter",
            "mode": "lines+markers",
            "name": "Mileage Over Time"
        },
        "bar_chart": {
            "x": x_values,
            "y": doors_values,
            "type": "bar",
            "name": "Number of Doors"
        },
        "scatter_chart": {
            "x": mileage_values,
            "y": kilometrage_values,
            "type": "scatter",
            "mode": "markers",
            "name": "Mileage vs Kilometrage"
        }
    }

    return JsonResponse(chart_data)

def d3_dashboard(request):
    return render(request, 'visualization/d3_dashboard.html')
