const jeawoo_arms = document.getElementById("jeawoo_arms");
const pillguk = document.getElementById("pillguk");
const press_on_button = document.getElementById("press_on")

press_on_button.addEventListener("click", function() {
    jeawoo_arms.classList.remove('press_on_jeawoo');
    pillguk.classList.remove('press_on_pillguk');
    jeawoo_arms.classList.add('press_on_jeawoo');
    pillguk.classList.add('press_on_pillguk');
})