fetch("http://127.0.0.1:8000/api/v1/rainfall/")
    .then(response => response.json())
    .then(data => {
        const months = Array.from({length: 12}, (item, i) => {
            return new Date(0, i).toLocaleString('en-GB', {month: 'short'})
        });
        const tokyoData = data.map(items => items.value).slice(0,12);
        const nyData = data.map(items => items.value).slice(12,24);
        const londonData = data.map(items => items.value).slice(24,36);
        const berlinData = data.map(items => items.value).slice(36,48);
        console.log(tokyoData)

        Highcharts.chart("rainfall-chart", {
            chart: {"type": "column"},
            title: {text: 'Monthly Average Rainfall'},
            credits: {"enabled": false},
            xAxis: {
                categories: months,
                crosshair: true
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Rainfall (mm)'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: 'Tokyo',
                data: tokyoData

            }, {
                name: 'New York',
                data: nyData

            }, {
                name: 'London',
                data: londonData

            }, {
                name: 'Berlin',
                data: berlinData

            }]
        });
    })
    .catch(error => {
        console.error('Error with fetch operation:', error);
    });