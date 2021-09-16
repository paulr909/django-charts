const survivedChart = document.querySelector("#survived-chart");

fetch(survivedChart.dataset.url)
    .then(response => response.json())
    .then(data => {
        Highcharts.chart("survived-chart", data);
    })
    .catch(error => {
        console.error('Error with fetch operation:', error);
    });
