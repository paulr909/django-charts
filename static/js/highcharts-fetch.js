// Highcharts.setOptions({
//     chart: {
//         style: {
//             fontFamily: "'Andale Mono', serif",
//             fontSize: 20
//         }
//     }
// });

// with Fetch API

fetch("http://127.0.0.1:8000/api/v1/browsers/")
    .then(response => response.json())
    .then(data => {
        const chartData = data.map(items => items);

        Highcharts.chart("chart-3", {
            "chart": {"type": "pie"},
            "title": {"text": "Browser Market Share Worldwide - August 2021"},
            "credits": {"enabled": false},
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