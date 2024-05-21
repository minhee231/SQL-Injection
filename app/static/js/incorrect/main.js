const ad_jw = document.getElementById("ad_jw");
const jeawo_ungood_hand = document.getElementById("jeawo_ungood_hand");

ad_jw.addEventListener("mouseover", function() {
    jeawo_ungood_hand.classList.add("jeawoo_hand_move");
});

ad_jw.addEventListener("mouseleave", function() {
    jeawo_ungood_hand.classList.remove("jeawoo_hand_move");
});