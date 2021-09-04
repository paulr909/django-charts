Highcharts.setOptions({
    chart: {
        style: {
            fontFamily: "'Andale Mono', serif",
            fontSize: 20
        }
    }
});

const chart3 = document.querySelector("#chart-3");

fetch(chart3.dataset.url)
    .then(response => response.json())
    .then(data => {
        Highcharts.chart("chart-3", data);
    })
    .catch(error => {
        console.error('Error with fetch operation:', error);
    });


const chart4 = document.querySelector("#chart-4");

fetch(chart4.dataset.url)
    .then(response => response.json())
    .then(data => {
        Highcharts.chart("chart-4", data);
    })
    .catch(error => {
        console.error('Error with fetch operation:', error);
    });