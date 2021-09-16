const chartPassengers = document.querySelector("#passengers-chart");

fetch("http://127.0.0.1:8000/api/v1/passengers/")
    .then(response => response.json())
    // .then(data => console.log(data))
    .then(data => {
        const names = data.map(items => items.name);
        const age = data.map(items => items.age);

        let ctx = chartPassengers.getContext("2d");
        new Chart(ctx, {
            type: 'pie',
            data: {
                datasets: [{
                    data: age,
                    backgroundColor: [
                        'rgb(0,191,255)',
                        'rgb(25,25,112)',
                        'rgb(138,43,226)',
                        'rgb(139,0,139)',
                        'rgb(216,191,216)',
                        'rgb(250,235,215)',
                    ],
                    label: 'Passengers'
                }],
                labels: names
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Passengers',
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
                tooltips: {
                    titleFontSize: 14,
                    bodyFontSize: 14,
                    titleFontFamily: "'Andale Mono', serif",
                    bodyFontFamily: "'Andale Mono', serif",
                },
                animation: {
                    duration: 2000,
                },
            }
        });
    })
    .catch(error => {
        console.error('Error with fetch operation:', error);
    });