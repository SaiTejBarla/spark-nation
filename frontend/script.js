const API_URL = "http://127.0.0.1:8000";

async function fetchData(endpoint, outputId) {
  const token = localStorage.getItem("token");
  const res = await fetch(`${API_URL}/${endpoint}/`, {
    headers: { "Authorization": `Bearer ${token}` }
  });
  const data = await res.json();
  document.getElementById(outputId).innerText = JSON.stringify(data, null, 2);
}

async function getStartups() { fetchData("startups", "startups-list"); }

async function evaluateAI() {
  const name = document.getElementById("eval-startup").value;
  const pitch = document.getElementById("eval-pitch").value;
  const res = await fetch(`${API_URL}/ai/evaluate`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({startup_name: name, pitch})
  });
  const data = await res.json();
  document.getElementById("ai-result").innerText = JSON.stringify(data, null, 2);
}
