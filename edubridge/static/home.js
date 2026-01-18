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
function openFeedbackModal() {
  document.getElementById("feedbackModal").style.display = "flex";
}

function closeFeedbackModal() {
  document.getElementById("feedbackModal").style.display = "none";
}

function submitFeedback() {
  const feedback = document.getElementById("teacherFeedback").value;

  if (!feedback.trim()) {
    alert("Please enter classroom feedback");
    return;
  }

  // Show loading state
  document.getElementById("aiResponse").classList.remove("hidden");
  document.getElementById("aiText").innerText = "Analyzing classroom issue with AI... 🤖";

  fetch("/features/analyze/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({
      text: feedback   // ✅ matches serializer
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("aiText").innerHTML = `
      <strong>Detected Issues:</strong><br>
      ${data.detected_issues.join(", ")}<br><br>

      <strong>Cluster Identified:</strong><br>
      <span class="cluster-badge">${data.cluster_result}</span><br><br>

      <strong>Suggested Action:</strong><br>
      Personalized micro-learning and adaptive strategies will be generated for this cluster.
    `;
  })
  .catch(err => {
  document.getElementById("aiText").innerText =
    "Please provide more detailed classroom feedback for accurate analysis.";
  console.error(err);
});

}


  // TEMP DEMO RESPONSE (replace with backend call)
  document.getElementById("aiResponse").classList.remove("hidden");
  document.getElementById("aiText").innerText =
    `Cluster Identified: Classroom Engagement\n\nSuggested Action:\n• Use activity-based examples\n• Apply micro-learning module on interactive teaching\n• Involve local context in lessons`;

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


function openMicroModuleModal() {
  document.getElementById("microModuleModal").style.display = "flex";
}

function closeMicroModuleModal() {
  document.getElementById("microModuleModal").style.display = "none";
}

function loadMicroModule() {
  const topic = document.getElementById("moduleTopic").value;
  const moduleText = document.getElementById("moduleText");

  // TEMP: Policy-based demo content (replace with backend later)
  const modules = {
    "Continuous Professional Development (CPD)": `
NEP 2020 mandates a minimum of 50 hours of Continuous Professional Development per year.
Teachers can fulfill this through workshops, peer learning, and online modules.
Focus is on improving classroom practices and student outcomes.
    `,

    "Student Engagement": `
NEP 2020 emphasizes activity-based and experiential learning.
Teachers are encouraged to move away from rote methods and
actively involve students in discussions and problem-solving.
    `,

    "Inclusive Classrooms": `
Policy highlights the need for inclusive strategies that address
diverse learning needs, languages, and socio-economic backgrounds.
Flexibility and empathy are key classroom practices.
    `,

    "Pedagogical Shift (NEP 2020)": `
NEP 2020 promotes a shift from content-heavy teaching
to conceptual understanding, critical thinking,
and learner-centered pedagogy.
    `
  };

  moduleText.innerText =
    modules[topic] || "No module available for this topic.";
}
