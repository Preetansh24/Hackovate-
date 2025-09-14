// Show sections
function showSection(section) {
    document.getElementById("dashboard-section").classList.add("hidden");
    document.getElementById("milk-section").classList.add("hidden");
    document.getElementById("disease-section").classList.add("hidden");

    document.getElementById(section + "-section").classList.remove("hidden");

    // Active nav link
    document.querySelectorAll(".nav-link").forEach(el => el.classList.remove("active"));
    document.querySelector(`[onclick="showSection('${section}')"]`).classList.add("active");
}

// ---------------- MILK PREDICTION ----------------
document.getElementById("milkForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    let data = {
        feed_kg: parseFloat(document.getElementById("feed_kg").value),
        temp_c: parseFloat(document.getElementById("temp_c").value),
        humidity: parseFloat(document.getElementById("humidity").value),
        milking_time: parseFloat(document.getElementById("milking_time").value)
    };

    try {
        let res = await fetch("http://127.0.0.1:8000/predict_milk", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        let result = await res.json();
        
        // Show milk prediction result
        document.getElementById("milkResult").classList.remove("hidden");
        document.getElementById("milkValue").innerText = result.predicted_yield.toFixed(2);

        // Fix confidence mismatch
        let confidencePercent = result.confidence > 1 ? result.confidence : result.confidence * 100;
        document.getElementById("milkConfidence").innerText = 
            "Confidence: " + confidencePercent.toFixed(2) + "%";

    } catch (err) {
        alert("Milk prediction failed: " + err);
    }
});

// ---------------- DISEASE PREDICTION ----------------
document.getElementById("diseaseForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    let data = {
        cow_id: document.getElementById("cow_id").value,
        day: parseInt(document.getElementById("day").value),
        months_after_birth: parseInt(document.getElementById("months_after_birth").value),
        previous_mastitis: parseInt(document.getElementById("previous_mastitis").value),
        temperature: parseFloat(document.getElementById("temperature").value),
        breed: document.getElementById("breed").value
    };

    try {
        let res = await fetch("http://127.0.0.1:8000/predict_disease", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        let result = await res.json();

        // Fix confidence mismatch
        let confidencePercent = result.confidence > 1 ? result.confidence : result.confidence * 100;

        // Show result + advice
        alert(
            "Disease Prediction: " + result.disease + 
            "\nConfidence: " + confidencePercent.toFixed(2) + "%" +
            (result.advice ? "\nAdvice: " + result.advice : "")
        );

    } catch (err) {
        alert("Disease prediction failed: " + err);
    }
});
