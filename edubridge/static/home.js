// Simple hover animation feedback
const cards = document.querySelectorAll(".feature-card");

cards.forEach(card => {
    card.addEventListener("mouseenter", () => {
        card.style.transform = "scale(1.03)";
        card.style.transition = "0.3s";
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = "scale(1)";
    });
});

document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".feature-card");

  cards.forEach(card => {
    card.addEventListener("mouseenter", () => {
      card.style.transform = "scale(1.03)";
    });

    card.addEventListener("mouseleave", () => {
      card.style.transform = "scale(1)";
    });
  });
});

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


function openFeedbackModal() {
  document.getElementById("feedbackModal").style.display = "flex";
}

function closeFeedbackModal() {
  document.getElementById("feedbackModal").style.display = "none";
}
function submitFeedback() {
  const feedback = document.getElementById("teacherFeedback").value.trim();
  const responseBox = document.getElementById("aiResponse");
  const responseText = document.getElementById("aiText");

  if (!feedback) {
    alert("Please enter classroom feedback");
    return;
  }

  // Loading state
  responseBox.classList.remove("hidden");
  responseText.innerText = "Analyzing classroom feedback using policy engine...";

  fetch("/api/analyze/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({ text: feedback })
  })
    .then(res => {
      if (!res.ok) {
        throw new Error("Backend error");
      }
      return res.json();
    })
    .then(data => {
      responseText.innerHTML = `
        <strong>Detected Issues</strong><br>
        ${data.detected_issues.join(", ") || "Not clearly identified"}<br><br>

        <strong>Cluster Identified</strong><br>
        <span class="cluster-badge">${data.cluster_result}</span><br><br>

        <strong>Next Step</strong><br>
        A personalized micro-learning module will be generated for this cluster.
      `;
    })
    .catch(() => {
      responseText.innerText =
        "Unable to analyze feedback. Please provide more detailed classroom input.";
    });
}

function openMicroModuleModal() {
  document.getElementById("microModuleModal").style.display = "flex";
}

function closeMicroModuleModal() {
  document.getElementById("microModuleModal").style.display = "none";
}

function loadMicroModule() {
  const topic = document.getElementById("moduleTopic").value;
  const moduleText = document.getElementById("moduleText");

  moduleText.innerText = "Loading micro-module from policy documents...";

  fetch("/api/micro-module/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({ topic })
  })
    .then(res => res.json())
    .then(data => {
      moduleText.innerHTML = `
        <h4>${data["Module Title"]}</h4>
        <p><strong>Objective:</strong> ${data["Learning Objective"]}</p>
        <p><strong>Key Concept:</strong> ${data["Key Concept"]}</p>
        <p><strong>Activity:</strong> ${data["Activity 1 (5 min)"]}</p>
        <p><strong>Reflection:</strong> ${data["Reflection Question"]}</p>
        <small>Source: ${data["Source"]}</small>
      `;
    })
    .catch(() => {
      moduleText.innerText = "Failed to load module";
    });
}

