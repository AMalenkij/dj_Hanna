const hamb = document.querySelector("#hamb");
const popup = document.querySelector("#popup");
const body = document.body;

// Clone the menu to set your own styles for the mobile version
const menu = document.querySelector("#menu").cloneNode(1);

// When clicking on the hamb icon, we call the hambHandler function
hamb.addEventListener("click", hambHandler);

// actions on click.
function hambHandler(e) {
  e.preventDefault();
  // Переключаем стили элементов при клике
  popup.classList.toggle("open");
  hamb.classList.toggle("active");
  body.classList.toggle("noscroll");
  renderPopup();
}

// Here we render elements in a popup
function renderPopup() {
  popup.appendChild(menu);
}

// Code to close the menu when the link is clicked
const links = Array.from(menu.children);

// For each menu item, when clicked, we call the function
links.forEach((link) => {
  link.addEventListener("click", closeOnClick);
});

// Closing the popup when clicking on the menu
function closeOnClick() {
  popup.classList.remove("open");
  hamb.classList.remove("active");
  body.classList.remove("noscroll");
}