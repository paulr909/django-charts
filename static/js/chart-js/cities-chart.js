// with Fetch API
const chartCities = document.querySelector("#cities-chart");

fetch("http://localhost:8000/api/v1/cities/")
    .then(response => response.json())
    // .then(data => console.log(data))
    .then(data => {
        const names = data.map(items => items.name);
        const population = data.map(items => items.population);

        let ctx = chartCities.getContext("2d");
        new Chart(ctx, {
            type: 'pie',
            data: {
                datasets: [{
                    data: population,
                    backgroundColor: [
                        'rgb(0,191,255)',
                        'rgb(25,25,112)',
                        'rgb(138,43,226)',
                        'rgb(139,0,139)',
                        'rgb(216,191,216)',
                        'rgb(250,235,215)',
                    ],
                    label: 'Population'
                }],
                labels: names
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Cities',
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
