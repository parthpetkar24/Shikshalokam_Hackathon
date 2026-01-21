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
        issue: description
    })
  })
    .then(async res => {
      const data = await res.json().catch(() => ({}));

      if (!res.ok) {
        console.error("BACKEND ERROR:", data);
        throw new Error("Backend error");
      }

      return data;
    })
    .then(data => {
      console.log("API RESPONSE:", data);

  if (!data || data.success === false) {
    throw new Error("Invalid backend response");
  }

  const clusterName =
    typeof data.cluster === "string"
      ? data.cluster
      : "Not identified";

  const feedbackText =
    typeof data.feedback === "string"
      ? data.feedback
      : "No policy-based feedback available.";

      responseText.innerHTML = `

        <strong>Cluster Identified</strong><br>
        <span class="cluster-badge">${clusterName}</span><br><br>

          <strong>AI Feedback</strong><br>
  ${feedbackText}
`;

      // Optional: store micro-module
      window.__MICRO_MODULE__ = data.micro_module;
    })
    .catch(err => {
      responseText.innerText = "An error occurred while analyzing the feedback.";
      console.error(err);
    });
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
