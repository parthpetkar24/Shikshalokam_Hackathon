// Dropdown logic
const dropdownBtn = document.querySelector(".dropdown-btn");
const dropdownMenu = document.querySelector(".dropdown-menu");

if (dropdownBtn) {
  dropdownBtn.addEventListener("click", () => {
    dropdownMenu.style.display =
      dropdownMenu.style.display === "block" ? "none" : "block";
  });
}

// Signup page logic
const params = new URLSearchParams(window.location.search);
const type = params.get("type");

const emailField = document.getElementById("emailField");
const mobileField = document.getElementById("mobileField");
const title = document.getElementById("title");

if (type === "email") {
  mobileField.style.display = "none";
  title.innerText = "Register with Email";
}

if (type === "mobile") {
  emailField.style.display = "none";
  title.innerText = "Register with Mobile";
}
