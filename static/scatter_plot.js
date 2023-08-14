// Fetch the wildfire data from the server and create scatter plot
fetch('/data', { mode: 'same-origin', credentials: 'same-origin' })
  .then(response => response.json())
  .then(data => {
    var latitudes = data.map(item => item.Latitude);
    var longitudes = data.map(item => item.Longitude);

    var plotData = [{
      x: longitudes,
      y: latitudes,
      mode: 'markers',
      type: 'scatter'
    }];

    var layout = {
      title: 'Wildfires',
      xaxis: { title: 'Longitude' },
      yaxis: { title: 'Latitude' }
    };

    Plotly.newPlot('plot', plotData, layout);
  })
  .catch(error => console.error('An error occurred:', error));
