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
  const clusterToModule = {
    "Teacher Professional Development": "cpd_overview",
    "Inclusive Education": "cpd_inclusive_practices",
    "Pedagogical Practices": "experiential_pedagogy"
  };

  const moduleKey = clusterToModule[clusterName];
  if (moduleKey) {
    fetchMicroModule(moduleKey);
  }

    })
    .catch(err => {
      responseText.innerText = "An error occurred while analyzing the feedback.";
      console.error(err);
    });
}


// -------------------- LOAD MICRO MODULE --------------------
function loadMicroModule() {
  const moduleText = document.getElementById("moduleText");
  const select = document.getElementById("moduleTopic");

  const selectedLabel = select.value;
  const topicMap = {
    "Continuous Professional Development (CPD)": "cpd_overview",
    "Student Engagement": "cpd_peer_learning",
    "Inclusive Classrooms": "cpd_inclusive_practices",
    "Pedagogical Shift (NEP 2020)": "experiential_pedagogy"
  };

  const topicKey = topicMap[selectedLabel];

  if (!topicKey) {
    moduleText.innerText = "Invalid module selection.";
    return;
  }

  moduleText.innerText = "Loading micro-learning module...";
  fetch("/api/micro-module/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({
      topic: topicKey
    })
  })
    .then(res => res.json())
    .then(data => {
      console.log("MICRO MODULE RESPONSE:", data);
      if (!data || !data.micro_module || !data.micro_module.module_content) {
  moduleText.innerText = "Unable to load micro-learning module.";
  return;
}

      const m = data.micro_module;
      moduleText.innerHTML = `
  <h3>${m.module_title}</h3>
  <p><strong>Source:</strong> ${m.policy_source}</p>

  ${m.policy_intent ? `<p><em>${m.policy_intent}</em></p>` : ""}

  <h4>Learning Objectives</h4>
  <ul>
    ${(m.learning_objectives || [])
      .map(obj => `<li>${obj}</li>`)
      .join("")}
  </ul>

  ${(m.module_content || [])
    .map(section => `
      <h4>${section.title}</h4>
      <ul>
        ${section.points.map(point => `<li>${point}</li>`).join("")}
      </ul>
    `)
    .join("")}

  <p><em>Estimated duration: ${m.duration}</em></p>
`;

    })
    .catch(err => {
      console.error("Micro-module fetch error:", err);
      moduleText.innerText = "Error loading micro-learning module.";
    });
}


