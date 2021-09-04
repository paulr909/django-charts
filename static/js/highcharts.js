Highcharts.setOptions({
    chart: {
        style: {
            fontFamily: "'Andale Mono', serif",
            fontSize: 20
        }
    }
});

// with Fetch API
const chart = document.querySelector("#chart-1");

fetch(chart.dataset.url)
    .then(response => response.json())
    .then(data => {
        Highcharts.chart("chart-1", data);
    })
    .catch(error => {
        console.error('Error with fetch operation:', error);
    });

// with jQuery AJAX
$.ajax({
    url: $("#chart-2").attr("data-url"),
    dataType: 'json',
    success: function (data) {
        Highcharts.chart("chart-2", data);
    }
});
