# Wildfire Application

**Project Description**
The Wildfire Application showcases real-time wildfire data through multiple visualizations such as an interactive map, heatmap, and scatter plot. It leverages the Flask framework for the backend and various front-end libraries including Google Maps, Leaflet, and Plotly for visualizations.

The application retrieves wildfire data from a given API endpoint, processes the data, and serves it to the frontend where the data gets visualized using the above-mentioned libraries.

**Project Structure:**
app.py: This file contains the backend code responsible for fetching data, processing it, and providing endpoints for the frontend.
heatmap.js: Contains code for generating a heatmap using Leaflet.
map.js: Uses the Google Maps API to display wildfire data as markers on a map.
scatterplot.js: Uses Plotly to display the wildfire data as a scatter plot.
wildfires.html: The main HTML template for the application, linking all visualization components.
styles.css: Contains styles for the HTML elements.

**How to Run the Project:**
Install the required Python packages:
```python
pip install -r requirements.txt
```
Start the Flask application: 
```python
flask run
```
Open a web browser and navigate to http://127.0.0.1:5000/ to view the application.
Ensure you have the appropriate permissions and API keys (e.g., for Google Maps) before running the application.