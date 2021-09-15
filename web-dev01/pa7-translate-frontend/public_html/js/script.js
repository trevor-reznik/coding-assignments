/**
 * PA7
 *
 * AJAX and CSS-toggling listeners.
 * Async AJAX listneer for keydown events in input fields.
 * Translating input using TranslateServer Express app instance from PA6.
 * Translation works left-to-right or right-to-left.
 * CSC337 | Summer 2021
 *
 * @author Christian P. Byrne
 *
 *
 */

const ResolveKeydown = async (target) => {
  /**
   * Handles keydown event within textareas.
   *
   * Void. Requests translation of input text from TranslateServer
   * then writes response text to corresponding output textarea wrapper.
   *
   * @param   {HTMLElement}     target  textarea that was clicked.
   * @listens document#keydown
   */
  identifyPanel(target)[0].innerHTML = await new Promise((resolve) => {
    /**
     * Promise constructor for translation API resposne.
     * @param   {() => Promise<string>}  executor  Resolve callback function.
     * @returns {Promise<string>}
     */
    const xhttp = new XMLHttpRequest();
    const languageCode = translationType(target);
    if (!languageCode || target.value.length < 2) {
      resolve(target.value); //  Copy and paste, don't translate.
    } else {
      const url = `http://127.0.0.1:5000/translate/${languageCode}/${target.value
        .toString()
        .replace(" ", "+")
        .toLowerCase()}`;
      xhttp.open("GET", url, true);
      xhttp.onload = () => {
        resolve(xhttp.responseText);
      };
      xhttp.send();
    }
  });
};

translationType = (target) => {
  /**
   * Returns appropriate 2nd arg in translation GET url.
   * @param   {HTMLElement}     target  Active textarea receiving input.
   * @returns {string || false}         GET param or false if same language.
   * @example If first dropdown value is 'German' and second is 'English':
   *  > translationType(textarea)
   *  "g2e"
   */
  let ret = Array.from(document.getElementsByTagName("select")).map((node) => {
    return node.value[0].toLowerCase();
  }); // It's like python's list comprehension but bad.
  return ret[0] === ret[1]
    ? false
    : target.getAttribute("id") == "left"
    ? `${ret[0]}2${ret[1]}`
    : `${ret[1]}2${ret[0]}`;
};

function echo(target) {
  /**
   * Echos textarea input to the associated wrapper.
   * @param   {HTMLElement}     target  Textarea that was clicked.
   * @listens document#keydown
   */
  identifyPanel(target)[2].innerHTML = target.value;
  identifyPanel(target)[1].classList.toggle("receiving");
  identifyPanel(target)[1].classList.toggle("receiving");
}

function activate(target) {
  /**
   * Toggle blinking-cursor psuedo class.
   * @param   {HTMLElement}   target  Textarea that was clicked.
   * @listens document#click
   */
  const [mirror, mirrorWrapper, targetWrapper] = identifyPanel(target);
  targetWrapper.classList.add("focus");
  target.parentElement.classList.remove("receiving");
  mirror.classList.remove("focus");
  mirrorWrapper.classList.add("receiving");
}

function identifyPanel(target) {
  /**
   * Returns the correct input/output elements based on the caller's ID.
   * @param   {HTMLElement} target  Textarea that was clicked.
   * @returns {Array<Node>}         Mirror, mirror's wrapper, target's wrapper.
   */
  const mirror =
    target.getAttribute("id") == "left"
      ? document.getElementById("right").parentElement.children[1]
      : document.getElementById("left").parentElement.children[1];
  return [mirror, mirror.parentElement, target.parentElement.children[1]];
}

function swapSelection() {
  /** Swaps 'value' attribute values of `select` tags */
  const selectNodes = document.getElementsByTagName("select");
  let selected = Array.from(selectNodes).map((node) => {
    return node.value;
  });
  let i = 1;
  for (let node of selectNodes) {
    node.value = selected[i];
    i--;
  }
}

function deFocus() {
  /** Remove blinking-cursor pseudo class when textarea is not focused. */
  for (const textarea of document.getElementsByTagName("textarea")) {
    if (textarea !== document.activeElement) {
      textarea.parentElement.children[1].classList.remove("focus");
    }
  }
}

window.onload = () => {
  /** Add event listeners @listens document#load */
  for (const input of document.getElementsByTagName("textarea")) {
    input.addEventListener("keydown", function () {
      setTimeout(() => {
        ResolveKeydown(this);
        echo(this);
      }, 100);
    });
    input.addEventListener("click", function () {
      activate(this);
    });
  }
  for (const select of document.getElementsByTagName("select")) {
    select.addEventListener("change", function () {
      ResolveKeydown(document.getElementById("left"));
    });
  }
  document
    .getElementsByTagName("svg")[0]
    .addEventListener("click", swapSelection);
  document.body.addEventListener("click", deFocus);
  document
    .getElementsByTagName("button")[0]
    .addEventListener("click", function () {
      /** Simple dark-mode toggler. */
      let ret = this.innerHTML == "Dark Mode" ? ["1", "Light"] : ["0", "Dark"];
      document.documentElement.setAttribute(
        "style",
        `filter: invert(${ret[0]});`
      );
      this.innerHTML = `${ret[1]} Mode`;
    });
};