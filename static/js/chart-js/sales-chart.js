const chartSales = document.querySelector("#sales-chart");

fetch("http://localhost:8000/api/v1/sales/")
    .then(response => response.json())
    // .then(data => console.log(data))
    .then(data => {
        const team = data.map(items => items.team_value);
        const ukData = data.map(items => items.value).slice(0, 12);
        const usData = data.map(items => items.value).slice(12, 24);
        const months = Array.from({length: 12}, (item, i) => {
            return new Date(0, i).toLocaleString('en-GB', {month: 'short'})
        });
        // console.log(ukData)

        let ctx = chartSales.getContext("2d");
        new Chart(ctx, {
            type: 'line',
            data: {
                datasets: [
                    {
                        label: team[0],
                        data: ukData,
                        borderColor: '#4daaf6',
                        backgroundColor: '#6ec3ec',
                    },
                    {
                        label: team[13],
                        data: usData,
                        borderColor: '#e50f28',
                        backgroundColor: '#ED678EFF',
                    }
                ],
                labels: months
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Sales Closed 2020',
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