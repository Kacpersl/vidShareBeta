const buttonRight = document.getElementById('slideRight');
const buttonLeft = document.getElementById('slideLeft');

buttonRight.onclick = function () {
document.getElementByClassName('row-scroll').scrollLeft += 20;
};
buttonLeft.onclick = function () {
document.getElementByClassName('row-scroll').scrollLeft -= 20;
};