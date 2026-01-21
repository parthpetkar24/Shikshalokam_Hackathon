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
function goToDIET() {
  window.location.href = "loginpage\\diet_login.html";
}

function goToTeacher() {
  window.location.href = "loginpage\\sign_up.html";
}

function goToLogin() {
  window.location.href = "loginpage\\teacher_login.html";
}
<script>
  function goToDashboard() {
    window.location.href = "dashboard/index.html";
  }
</script>

