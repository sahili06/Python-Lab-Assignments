import pandas as pd

data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Karnataka", "Tamil Nadu"],
    "Area": [307713, 196244, 342239, 191791, 130058],
    "Population": [124000000, 70000000, 81000000, 68000000, 78000000]
}

df = pd.DataFrame(data)

print("Complete Information of States:\n")
print(df.to_string(index=False))

largest_area_state = df.loc[df['Area'].idxmax(), 'State']
print("\nState with Largest Area:", largest_area_state)

largest_population_state = df.loc[df['Population'].idxmax(), 'State']
print("State with Largest Population:", largest_population_state)

df['Population_Density'] = df['Population'] / df['Area']

print("\nStates with Population Density:\n")
print(df.to_string(index=False))

highest_density_state = df.loc[df['Population_Density'].idxmax(), 'State']
print("\nState with Highest Population Density:", highest_density_state)
