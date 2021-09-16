// with jQuery AJAX
$(function () {
    let $populationChartData = $("#population-chart");
    $.ajax({
        url: $populationChartData.data("url"),
        success: function (data) {
            let ctx = $populationChartData[0].getContext("2d");
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Population',
                        backgroundColor: [
                            'rgb(255, 99, 132)',
                            'rgb(54, 162, 235)',
                            'rgb(255, 205, 86)',
                            'rgb(255,127,80)',
                            'rgb(184,134,11)',
                            'rgb(189,183,107)',
                            'rgb(154,205,50)',
                            'rgb(0,100,0)',
                            'rgb(47,79,79)',
                            'rgb(0,139,139)',
                            'rgb(0,255,255)',
                            'rgb(100,149,23)',
                            'rgb(0,191,255)',
                            'rgb(25,25,112)',
                            'rgb(138,43,226)',
                            'rgb(139,0,139)',
                            'rgb(216,191,216)',
                            'rgb(250,235,215)',
                            'rgb(139,69,19)',
                            'rgb(244,164,96)',
                            'rgb(188,143,143)',
                            'rgb(255,228,225)',
                            'rgb(112,128,144)',
                            'rgb(230,230,250)',
                            'rgb(128,0,0)',
                            'rgb(220,20,60)',
                            'rgb(205,92,92)',
                            'rgb(255,69,0)',
                            'rgb(184,134,11)',
                        ],
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Country Population',
                        fontSize: 20,
                        fontFamily: "'Andale Mono', serif",
                    },
                    legend: {
                        position: 'top',
                        labels: {
                            fontSize: 20,
                            fontFamily: "'Andale Mono', serif",
                        }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                fontSize: 14,
                                fontFamily: "'Andale Mono', serif"
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                fontSize: 14,
                                fontFamily: "'Andale Mono', serif"
                            }
                        }]
                    },
                    tooltips: {
                        titleFontSize: 14,
                        bodyFontSize: 14,
                        titleFontFamily: "'Andale Mono', serif",
                        bodyFontFamily: "'Andale Mono', serif",
                    },
                    animation: {
                        duration: 2000,
                    }
                }
            });
        }
    });
});
