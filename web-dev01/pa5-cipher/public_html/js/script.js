/**
 * Script for cipher assignment.
 *
 * Handles encrypting input, updating slider value indicator, creating
 * and appending the table, shuffling the table cells, and adding event
 * listeners. I did not use any jQuery for this assignment.
 *
 * @author Christian P. Byrne
 */

function shuffleSquare() {
  /**
   * Void. Updates alphabet table with randomly ordered letters.
   *
   * Calls refreshDisplay.
   */

  var alphabet = Array.from("abcdefghijklmnopqrstuvwxy");
  for (var i = 0; i < 25; i++) {
    // Random index of remaining letters -> write to html -> pop letter.
    let ranNum = Math.floor(Math.random() * alphabet.length);
    document.getElementsByTagName("td")[i].innerHTML = alphabet[ranNum];
    alphabet.splice(ranNum, 1);
  }
  refreshDisplay();
}

function encrypt(keyAlphabet, divNum) {
  /**
   * Void. Encrypts text from input field based on indexes in keyAlphabet.
   * Uses index of each letter in original alphabet and replaces letter with
   * letter from same index in keyAlphabet. Posts encrypted version of string
   * to specified div.
   *
   * @param {Array}   keyAlphabet 26 string elements representing letters in 
   *                                shuffled alphabet.
   * @param {Number}  divNum      Index of div in body.children to display 
   *                                output to.
   */

  var alphabet = "abcdefghijklmnopqrstuvwxyz";
  var encrypted = "";
  for (var letter of document
    .getElementsByTagName("input")
    [0].value.toLowerCase()) {
    // Skip if letter is not alpha or is a z (for 2nd cipher).
    if (!alphabet.includes(letter) || (divNum === 1 && letter === "z")) {
      encrypted += letter;
    } else {
      // Use index of letter in alphabet and get same index elem in keyAlphabet.
      encrypted += keyAlphabet[alphabet.indexOf(letter)];
    }
  }
  document.body.children[divNum].innerHTML = encrypted;
}

function refreshDisplay() {
  /**
   * Updates encryption output and range indicator.
   *
   * Void. Creates shuffled alphabet based on the two cipher algorithms.
   * Then calls encrypt function by passing the appropriate cipher key
   * alphabet and the div number associated with that cipher.
   *
   * @listens document#keydown
   * @listens document#onchange
   * @listens document#onclick
   */
  document.getElementsByTagName("span")[0].innerText =
    document.getElementsByTagName("input")[1].value;
  setTimeout(function () {
    var cipherKey = Array.from("abcdefghijklmnopqrstuvwxyz");
    for (var i = document.getElementsByTagName("input")[1].value; i > 0; i--) {
      let a = cipherKey[0];
      cipherKey.push(a);
      cipherKey.shift();
    }
    encrypt(cipherKey, 1);
    cipherKey = [];
    for (var cell of document.getElementsByTagName("td")) {
      cipherKey.push(cell.innerHTML);
    }
    encrypt(cipherKey, 2);
  }, 200);
}

window.onload = function () {
  /**
   * Initializes table and event attributes.
   *
   * Initializes the alphabet table by creating the table and filling
   * in cells with alphabet letters. Sets event attributes for the input
   * and button nodes.
   *
   * @listens window#onload
   */
  var alphabet = Array.from("abcdefghijklmnopqrstuvwxyz");
  var table = document.createElement("table");
  for (var i = 0; i < 5; i++) {
    var row = table.insertRow(i);
    for (var r = 0; r < 5; r++) {
      let cell = row.insertCell(r);
      // Fill in cell with first value, then shift the alphabet array.
      cell.innerHTML = alphabet[0];
      alphabet.shift();
    }
  }
  document.querySelectorAll("div")[0].appendChild(table);

  // Set event attributes.
  document.getElementsByTagName("input")[0].focus();
  document
    .getElementsByTagName("input")[0]
    .setAttribute("onkeydown", "refreshDisplay()");
  document
    .getElementsByTagName("input")[1]
    .setAttribute("onchange", "refreshDisplay()");
  document
    .getElementsByTagName("button")[0]
    .setAttribute("onclick", "shuffleSquare()");
};
