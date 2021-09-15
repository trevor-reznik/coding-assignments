/* Name: Christian P. Byrne
 * Course: CSC337
 * Description: Appends CSS for 10 :hover classes with background colors along a gradient created by
 *              parameter color then appends CSS to head. Cycles through class list on hover of input elements.
 *              Also makes lables right-alligned on hover of associated input field.
 */

$(document).ready(function () {
  var colors = [];
  for (var i = 10; i <= 99; i = i + 5) {
    colors.push(`hexff${Math.floor(i / 9)}b${i}`);
  }

  for (const color of colors) {
    let hoverClass = document.createElement("style");
    hoverClass.innerHTML = `.${color}:hover { background-color: ${color.replace(
      "hex",
      "#"
    )}; }`;
    document.getElementsByTagName("head")[0].appendChild(hoverClass);
  }

  $("input").mouseover(function () {
    var row = this.parentNode.parentNode.children;
    var index = Array.prototype.indexOf.call(row, this.parentNode);
    var f = $("#fields").children();
    for (var i = 0; i < $("#fields").children().length; i++) {
      let align = "left";
      if (i == index) {
        align = "right";
      }
      f[i].style.textAlign = align;
    }
  });

  $("input").hover(() => {
    var currClass =
      document.getElementsByTagName("input")[0].classList[0] || colors[0];
    var nxtClass =
      colors.indexOf(currClass) + 2 < colors.length
        ? colors[colors.indexOf(currClass) + 1]
        : colors[0];
    switchGlowColor(currClass, nxtClass);
  });
});

function switchGlowColor(curr, next) {
  for (const input of document.getElementsByTagName("input")) {
    if (!!input.classList) {
      input.classList.remove(curr);
    }
    input.classList.add(next);
  }
}
