const button = document.querySelector(".mobile-menu-button");
const menu = document.querySelector(".mobile-menu");
const icon = button.querySelector("i");

button.addEventListener("click", () => {
  menu.classList.toggle("active");

  button.classList.toggle("active");

  icon.classList.toggle("ti-menu-2");
  icon.classList.toggle("ti-x");
});
