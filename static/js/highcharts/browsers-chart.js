fetch("http://localhost:8000/api/v1/browsers/")
    .then(response => response.json())
    .then(data => {
        const chartData = data.map(items => items);

        Highcharts.chart("browsers-chart", {
            chart: {type: "pie"},
            title: {text: "Browser Market Share Worldwide - August 2021"},
            credits: {enabled: false},
            series: [{
                name: 'Browser',
                colorByPoint: true,
                data: chartData
            }],
        });
    })
    .catch(error => {
        console.error('Error with fetch operation:', error);
    });