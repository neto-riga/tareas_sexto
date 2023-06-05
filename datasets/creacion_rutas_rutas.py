import pandas as pd
import random

# Define the zones for each route
zones = {
    "ruta001": 1,
    "ruta002": 1,
    "ruta003": 1,
    "ruta004": 2,
    "ruta005": 2,
    "ruta006": 1,
    "ruta007": 1,
    "ruta008": 2,
}

# List all routes
routes = list(zones.keys())

# List for storing rows
rows = []

# Generate relations
for i, id1 in enumerate(routes):
    for id2 in routes[i+1:]:
        if id1 != id2:
            if zones[id1] == zones[id2]:
                distancia = random.randint(5, 35)
            else:
                distancia = random.randint(395, 425)

            # Append row
            rows.append([id1, id2, distancia])
            rows.append([id2, id1, distancia])

# Create DataFrame
df = pd.DataFrame(rows, columns=['id1', 'id2', 'distancia'])

# Save as CSV
df.to_csv('routes.csv', index=False)
