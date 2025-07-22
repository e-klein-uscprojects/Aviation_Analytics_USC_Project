import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
from geopy.distance import geodesic
import matplotlib.pyplot as plt

# Define coordinates for LAX and JFK
lax_coords = (33.9416, -118.4085)  # Los Angeles International Airport
jfk_coords = (40.6413, -73.7781)   # John F. Kennedy International Airport

# Create a DataFrame with the route
route_df = pd.DataFrame({
    'airport': ['LAX', 'JFK'],
    'latitude': [lax_coords[0], jfk_coords[0]],
    'longitude': [lax_coords[1], jfk_coords[1]]
})

# Create a LineString for the flight path
line = LineString([(lax_coords[1], lax_coords[0]), (jfk_coords[1], jfk_coords[0])])
gdf = gpd.GeoDataFrame(route_df, geometry=[line, line])
gdf.crs = "EPSG:4326"

# Calculate distance and fatigue index
distance_km = geodesic(lax_coords, jfk_coords).kilometers
fatigue_index = "High" if distance_km > 3000 else "Moderate"

# Print results
print(f"Flight Route: LAX ➜ JFK")
print(f"Distance: {round(distance_km, 2)} km")
print(f"Estimated Fatigue Index: {fatigue_index}")

# Plot the route
fig, ax = plt.subplots(figsize=(8, 6))
gdf.plot(ax=ax, color='blue', linewidth=2)
plt.title("Flight Route: LAX to JFK")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
