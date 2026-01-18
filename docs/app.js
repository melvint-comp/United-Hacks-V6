async function analyze() {
  const input = document.getElementById("chatInput").value;
  const output = document.getElementById("output");

  try {
    const parsed = JSON.parse(input);

    const response = await fetch("http://localhost:8000/analyze/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: parsed.messages })
    });

    const data = await response.json();
    output.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    output.textContent = "Invalid JSON or server not running.";
  }
}
