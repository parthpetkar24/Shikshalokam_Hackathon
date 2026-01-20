// -------------------- UI Animations --------------------
document.querySelectorAll(".feature-card").forEach(card => {
  card.addEventListener("mouseenter", () => {
    card.style.transform = "scale(1.03)";
    card.style.transition = "0.3s";
  });

  card.addEventListener("mouseleave", () => {
    card.style.transform = "scale(1)";
  });
});

// -------------------- CSRF Helper --------------------
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// -------------------- Modal Controls --------------------
function openFeedbackModal() {
  document.getElementById("feedbackModal").style.display = "flex";
}

function closeFeedbackModal() {
  document.getElementById("feedbackModal").style.display = "none";
}

function openMicroModuleModal() {
  document.getElementById("microModuleModal").style.display = "flex";
}

function closeMicroModuleModal() {
  document.getElementById("microModuleModal").style.display = "none";
}

// -------------------- ANALYZE FEEDBACK --------------------
function submitFeedback() {
  const description = document.getElementById("teacherFeedback").value.trim();
  const responseBox = document.getElementById("aiResponse");
  const responseText = document.getElementById("aiText");

  if (!description) {
    alert("Please describe what is happening in your classroom.");
    return;
  }

  responseBox.classList.remove("hidden");
  responseText.innerText = "Analyzing classroom input using EduBridge AI...";

  fetch("/api/analyze/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({
      description: description
    })
  })
    .then(async res => {
  const data = await res.json().catch(() => ({}));

  if (!res.ok) {
    console.error("BACKEND ERROR:", data);
    return data; // let UI show backend message
  }

  return data;
})
    .then(data => {
      // ---- Detected Issues ----
      const issues = data.detected_issues?.map(i => i.name).join(", ")
        || "Not clearly identified";

      // ---- Cluster ----
      const clusterName = data.cluster?.cluster_name || "Not identified";

      responseText.innerHTML = `
        <strong>Detected Issues</strong><br>
        ${issues}<br><br>

        <strong>Cluster Identified</strong><br>
        <span class="cluster-badge">${clusterName}</span><br><br>

        <strong>AI Feedback</strong><br>
        ${data.feedback?.feedback?.[0]?.feedback || "Policy-based guidance generated."}
      `;

      // Store micro-module for next step
      window.__MICRO_MODULE__ = data.micro_module;
    })
}

// -------------------- LOAD MICRO MODULE --------------------
function loadMicroModule() {
  const moduleText = document.getElementById("moduleText");

  if (!window.__MICRO_MODULE__) {
    moduleText.innerText = "No micro-module available.";
    return;
  }

  const module = window.__MICRO_MODULE__;

  moduleText.innerHTML = `
    <h4>${module.title}</h4>
    <p><strong>Duration:</strong> ${module.duration_minutes} minutes</p>
    <p><strong>Objectives:</strong></p>
    <ul>
      ${module.objectives.map(o => `<li>${o}</li>`).join("")}
    </ul>
  `;
}
