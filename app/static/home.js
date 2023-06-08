// home.js
const sections = document.querySelectorAll("section");

function scrollToSection(event) {
    event.preventDefault();
    const targetId = event.target.getAttribute("href");
    const targetSection = document.querySelector(targetId);
    window.scrollTo({
        top: targetSection.offsetTop,
        behavior: "smooth"
    });
}

sections.forEach(section => {
    const link = section.querySelector("a");
    link.addEventListener("click", scrollToSection);
});
