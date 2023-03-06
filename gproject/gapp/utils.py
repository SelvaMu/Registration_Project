import pandas as pd
from django.http import HttpResponse
from . import models

def export_to_csv(model, filename):
    # Get all objects from the model
    objects = model.objects.all()

    # Convert the model data to a Pandas DataFrame
    data = pd.DataFrame(list(objects.values()))

    # Create a CSV response object
    response = HttpResponse(content_type='text/csv')

    # Set the CSV file name
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    # Write the DataFrame to the response as CSV
    data.to_csv(response, index=False)

    return response