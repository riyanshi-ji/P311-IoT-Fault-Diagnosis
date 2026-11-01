
let temperatureChart;
let vibrationChart;
let currentChart;


// ============================
// Create Charts
// ============================

function createCharts() {

    const commonOptions = {

        responsive: true,

        animation: false,

        scales: {

            x: {
                title: {
                    display: true,
                    text: "Time"
                }
            }

        }

    };


    temperatureChart = new Chart(
        document.getElementById("temperatureChart"),
        {
            type: "line",

            data: {
                labels: [],
                datasets: [{
                    label: "Temperature °C",
                    data: [],
                    tension: 0.3
                }]
            },

            options: commonOptions
        }
    );


    vibrationChart = new Chart(
        document.getElementById("vibrationChart"),
        {
            type: "line",

            data: {
                labels: [],
                datasets: [{
                    label: "Vibration",
                    data: [],
                    tension: 0.3
                }]
            },

            options: commonOptions
        }
    );


    currentChart = new Chart(
        document.getElementById("currentChart"),
        {
            type: "line",

            data: {
                labels: [],
                datasets: [{
                    label: "Current A",
                    data: [],
                    tension: 0.3
                }]
            },

            options: commonOptions
        }
    );
}


// ============================
// Load Dashboard Data
// ============================

async function loadData() {

    try {

        const latestResponse =
            await fetch(
                "http://127.0.0.1:5000/api/latest"
            );


        const latest =
            await latestResponse.json();


        const historyResponse =
            await fetch(
                "http://127.0.0.1:5000/api/history"
            );


        const history =
            await historyResponse.json();


        // ============================
        // Connection indicator
        // ============================

        document.getElementById(
            "connectionDot"
        ).style.background = "#22c55e";


        document.getElementById(
            "connectionText"
        ).textContent = "System Online";


        // ============================
        // Latest information
        // ============================

        document.getElementById(
            "machineId"
        ).textContent = latest.machine_id;


        document.getElementById(
            "timestamp"
        ).textContent = latest.timestamp;


        document.getElementById(
            "temperature"
        ).textContent = latest.temperature.toFixed(2);


        document.getElementById(
            "vibration"
        ).textContent = latest.vibration.toFixed(2);


        document.getElementById(
            "current"
        ).textContent = latest.current.toFixed(2);


        // ============================
        // Status
        // ============================

        const statusElement =
            document.getElementById("status");


        statusElement.textContent =
            latest.status;


        if (latest.status === "NORMAL") {

            statusElement.style.color = "#16a34a";

        }

        else if (latest.status === "WARNING") {

            statusElement.style.color = "#d97706";

        }

        else {

            statusElement.style.color = "#dc2626";

        }


        // ============================
        // Faults
        // ============================

        const faultsElement =
            document.getElementById("faults");


        if (latest.faults.length === 0) {

            faultsElement.innerHTML =
                "✅ No faults detected";

        }

        else {

            faultsElement.innerHTML =
                latest.faults
                    .map(
                        fault => `⚠️ ${fault}`
                    )
                    .join("<br>");
        }


        // ============================
        // Charts
        // ============================

        const readings =
            [...history].reverse();


        const labels =
            readings.map(
                item => item.timestamp.substring(11, 19)
            );


        temperatureChart.data.labels = labels;

        temperatureChart.data.datasets[0].data =
            readings.map(
                item => item.temperature
            );


        vibrationChart.data.labels = labels;

        vibrationChart.data.datasets[0].data =
            readings.map(
                item => item.vibration
            );


        currentChart.data.labels = labels;

        currentChart.data.datasets[0].data =
            readings.map(
                item => item.current
            );


        temperatureChart.update();

        vibrationChart.update();

        currentChart.update();


        // ============================
        // History table
        // ============================

        const table =
            document.getElementById(
                "historyTable"
            );


        table.innerHTML = "";


        history.forEach(item => {

            const row =
                document.createElement("tr");


            let faults =
                item.faults.length > 0
                    ? item.faults.join(", ")
                    : "None";


            row.innerHTML = `
                <td>${item.timestamp}</td>

                <td>${item.temperature.toFixed(2)} °C</td>

                <td>${item.vibration.toFixed(2)}</td>

                <td>${item.current.toFixed(2)} A</td>

                <td>${item.status}</td>

                <td>${faults}</td>
            `;


            table.appendChild(row);

        });

    }


    catch (error) {

        console.error(error);


        document.getElementById(
            "connectionDot"
        ).style.background = "#dc2626";


        document.getElementById(
            "connectionText"
        ).textContent = "System Offline";

    }
}


// ============================
// Start Dashboard
// ============================

createCharts();

loadData();


// Update every 3 seconds

setInterval(
    loadData,
    3000
);
