$(document).ready(function () {
    var heatmapMap = L.map('heatmap').setView([0, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(heatmapMap);

    $.getJSON('/heatmap', function (data) {
        var heatmapData = data.heatmap_data;
        L.heatLayer(heatmapData, {
            radius: 25,
            blur: 15,
            maxZoom: 10,
            gradient: {
                0.2: 'blue',
                0.4: 'cyan',
                0.5: 'lime',
                0.6: 'yellow',
                0.7: 'orange',
                0.8: 'red',
                1: 'darkred'
            },
            minOpacity: 0.5
        }).addTo(heatmapMap);
    });
});