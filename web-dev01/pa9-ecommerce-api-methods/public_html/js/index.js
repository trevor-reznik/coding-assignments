/**
 * Makeshift template engine for Ostaa app.
 * @author Christian P. Byrne
 */

import { apiRender, apiHandlers } from "./api.js";
import { loginRender, loginHandlers } from "./login.js";
import { homeRender, homeHandlers } from "./home.js";
const BASE_URL = "http://127.0.0.1:5000";

window.onload = () => {
  let dynamicStyle = document.createElement("link");
  dynamicStyle.rel = "stylesheet";
  dynamicStyle.data = "dynamic";
  document.querySelector("head").appendChild(dynamicStyle);
  // if (sessionStorage.getItem("login")) {
  //   renderPage("home")
  // }
  // else {
  //   renderPage("login")
  // }
  renderPage("api")
};

function renderPage(page) {
  if (page === "api") {
    apiRender();
    apiHandlers();
  } else if (page === "login") {
    loginRender();
    loginHandlers();
  } else if (page === "home") {
      homeRender();
      homeHandlers();
  }
}

class TemplateEngine {
  constructor(title) {
    this.clearDOM();
    this.left = this.dialogBox("left");
    this.right = this.dialogBox("right");
    this.footer = this.dialogBox("footer");
    this.header = this.dialogBox("header");
    this.left.appendChild(this.toolbar(title));
    document.body.appendChild(this.left);
    document.body.appendChild(this.right);

    this.useHeader = () => {
      document.body.prepend(this.header);
    };
    this.useFooter = () => {
      document.body.appendChild(this.footer);
    };
    this.push = (node, prepend, axis) => {
      if (node.length && node.length > 1) {
        for (let nodeElem of node) {
          if (!prepend) {
            this[axis].appendChild(nodeElem);
          } else {
            this[axis].prepend(nodeElem);
          }
        }
      } else {
        if (!prepend) {
          this[axis].appendChild(node);
        } else {
          this[axis].prepend(node);
        }
      }
    };
    this.addLeft = (node, prepend = false) => {
      this.push(node, prepend, "left");
    };
    this.addRight = (node, prepend = false) => {
      this.push(node, prepend, "right");
    };
  }
  updateStylesheet = (href) => {
    let links = document.querySelectorAll("link");
    for (let link of links) {
      if (link.data === "dynamic") {
        link.href = href;
      }
    }
  };
  dialogBox = (mainId = "main") => {
    let main = document.createElement("div");
    main.setAttribute("id", mainId);
    return main;
  };
  toolbar = (titleText = "Welcome") => {
    let header = document.createElement("header");
    let h6 = document.createElement("h6");
    h6.innerHTML = titleText;
    header.appendChild(h6);
    let buttonTray = document.createElement("div");

    const btnClasses = ["minimize-icon", "unmaximize-icon", "close-icon"];
    for (let cssClass of btnClasses) {
      let icon = document.createElement("span");
      icon.classList.add(cssClass);
      buttonTray.appendChild(icon);
    }
    header.appendChild(buttonTray);
    return header;
  };
  interactionBox = (title, titleCaption = false) => {
    let div = document.createElement("div");
    if (titleCaption) {
      let caption = document.createElement("b");
      caption.innerHTML = titleCaption;
      div.appendChild(caption);
    }
    div.innerHTML += title;
    return div;
  };
  inputBox = (options) => {
    let defaults = {
      type: "submit",
      value: "",
      name: "",
      id: "",
      placeholder: "Enter value. . .",
      label: false,
    };
    Object.assign(defaults, options);
    let input = document.createElement("input");
    for (const [property, value] of Object.entries(defaults)) {
      input.setAttribute(property, value);
    }
    if (defaults.label) {
      let labelNode = document.createElement("label");
      labelNode.innerHTML = defaults.label;
      labelNode.for = defaults.id;
      return [input, labelNode];
    }
    return input;
  };
  form = (options) => {
    let defaults = {
      id: false,
      method: false,
      action: false,
    };
    Object.assign(defaults, options);
    let formNode = document.createElement("form");
    for (const [property, value] of Object.entries(defaults)) {
      if (value) {
        formNode.setAttribute(property, value);
      }
    }
    return formNode;
  };
  boxesFromArray = (argArray) => {
    const ret = [];
    for (const boxOptions of argArray) {
      ret.push(this.interactionBox(...boxOptions));
    }
    return ret;
  };
  /**
   * Construct collection of input nodes and append to container.
   * Pass a contianer div and an array of options objects.
   * @param {HTMLElement}   container
   * @param {object}        options
   * */
  batchAppendInputs = (container, options) => {
    for (const optionObj of options) {
      let input = this.inputBox(optionObj);
      if (input.length && input.length > 1) {
        container.appendChild(input[1]);
        container.appendChild(input[0]);
      } else {
        container.appendChild(input);
      }
    }
  };
  loginForm = (title, caption, formId = "user") => {
    const formContainer = this.interactionBox(title, caption);
    const form = this.form({ id: formId });
    const formFields = [
      { type: "text", name: "username", id: "username", label: "Username" },
      { type: "password", name: "password", id: "password", label: "Password" },
      { type: "button", value: "Submit" },
    ];
    this.batchAppendInputs(form, formFields);
    formContainer.appendChild(form);
    return formContainer;
  };
  listingForm = (title, caption) => {
    const formContainer = this.interactionBox(title, caption);
    const form = this.form({ id: "item" });
    const formFields = [
      { type: "text", name: "title", id: "title", label: "Title" },
      {
        type: "text",
        name: "description",
        id: "description",
        label: "Description",
      },
      { type: "text", name: "image", id: "image", label: "Image" },
      { type: "number", name: "price", id: "price", label: "Price" },
      { type: "text", name: "stat", id: "stat", label: "Stat" },
      { type: "button", value: "Submit" },
    ];
    this.batchAppendInputs(form, formFields);
    formContainer.appendChild(form);
    return formContainer;
  };
  searchField = (type) => {
    let boxArgs;
    let inputFields;
    if (type === "users") {
      boxArgs = ["Search Users", "GET"];
      inputFields = [
        { type: "text", placeholder: "enter keyword..." },
        { id: "searchU", value: "Search" },
      ];
    } else if (type === "search-items") {
      boxArgs = ["Search Listings", "SHOP"];
      inputFields = [
        { type: "text", placeholder: "enter keyword..." },
        { id: "searchI", value: "Search" },
      ];
    } else if (type === "items") {
      boxArgs = ["Search Items", "GET"];
      inputFields = [
        { type: "text", placeholder: "enter keyword..." },
        { id: "searchI", value: "Search" },
      ];
    } else if (type === "home purchases") {
      boxArgs = ["View Your Purchases", "PROFILE"];
      inputFields = [
        { id: "my-purchases", value: "Get Purchase History" },
      ];
    } else if (type === "home listings") {
      boxArgs = ["View Your Listings", "PROFILE"];
      inputFields = [
        { id: "my-listings", value: "Get Listings History" },
      ];
    } else if (type === "user listings") {
      boxArgs = ["User's Listings", "GET"];
      inputFields = [
        { type: "text", placeholder: "enter username..." },
        { id: "listings", value: "Get Listings" },
      ];
    } else if (type === "user purchases") {
      boxArgs = ["User's Purchases", "GET"];
      inputFields = [
        { type: "text", placeholder: "enter username..." },
        { id: "purchases", value: "Get Purchases" },
      ];
    }
    const container = this.interactionBox(...boxArgs);
    this.batchAppendInputs(container, inputFields);
    return container;
  };
  clearDOM = () => {
    let root = document.querySelectorAll("body > div");
    for (let node of root) {
      node.remove();
    }
    document.body.remove();
    let newBody = document.createElement("body");
    document.documentElement.appendChild(newBody);
  };
}

export { TemplateEngine, BASE_URL, renderPage };
