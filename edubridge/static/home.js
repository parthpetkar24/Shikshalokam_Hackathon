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
  const issue = document.getElementById("issueType").value;

  if (!feedback.trim()) {
    alert("Please enter classroom feedback");
    return;
  }

  // TEMP DEMO RESPONSE (replace with backend call)
  document.getElementById("aiResponse").classList.remove("hidden");
  document.getElementById("aiText").innerText =
    `Cluster Identified: Classroom Engagement\n\nSuggested Action:\n• Use activity-based examples\n• Apply micro-learning module on interactive teaching\n• Involve local context in lessons`;

  // 🔜 BACKEND VERSION (later)
  /*
  fetch("/api/feedback/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ issue, feedback })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("aiText").innerText = data.response;
  });
  */
}


