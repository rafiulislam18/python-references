from django.shortcuts import render,HttpResponse
import pandas as pd

# Create your views here.

def show_food_list(request):
    data = pd.read_excel('foods/assets/sample_data.xlsx',sheet_name="SalesOrders")
    selected_col = ['Region', 'Unit Cost', 'Total']
    # foods = data.head(10).to_dict(orient='records')
    # foods = data[selected_col].sort_values(['Total'],ascending=False).head(100).to_dict(orient='records')
    sort_data = data[selected_col].sort_values(['Total'],ascending=False)
    filtered_data = sort_data[(sort_data['Total'] > 100) & (sort_data['Total'] < 500)]
    foods = filtered_data.head(100).to_dict(orient='records')
    # data.shape, data.tail()
    return render(request, 'food_list.html', context={'foods':foods})
