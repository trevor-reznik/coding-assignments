/**
 * PA7 | CSC337 Summer 2021
 *
 * Express app that responds to GET requests by translating param
 * and sending translated words in response content. The dictionaries 
 * take a while to build; I don't really know how to optimize it.
 * Express module not included.
 *
 * @author Christian P. Byrne
 *
 *
 */

const fetch = require("node-fetch");
const express = require("express");

async function mapTranslations(url) {
  /**
   * Fetches text data from benjdd.com translation dictionary files.
   * @param   {string}  url
   * @returns {Promise<[fromEng: {}, toEng:{}]>}
   */
  return fetch(url)
    .then((response) => response.text())
    .then(async (text) => {
      return await jsonifyRes(text);
    });
}

function jsonifyRes(text) {
  /**
   * Parses and maps translation source data.
   *
   * Handling duplicates (comma-separated synonyms) in source data:
   * - Use words.split(",").forEach() on keys.
   * - Use first word for values.
   *
   * @param {string}  text  text data from translation dictionary file.
   * @returns {[fromEng: {[key:string]:string}, toEng:{[key:string]:string}]}
   *
   */
  const lines = text.toLowerCase().split("\n");
  let toEng = {};
  let fromEng = {};
  for (const line of lines) {
    const left = line.split("\t")[0].trim();
    const right = line
      .split("\t")
      [line.split("\t").length - 1].split("[")[0]
      .split("(")[0]
      .replace("/n", "")
      .trim();
    left
      .split(",")
      .forEach((word) => (fromEng[word.trim()] = right.split(",")[0].trim()));
    right
      .split(",")
      .forEach((word) => (toEng[word.trim()] = left.split(",")[0].trim()));
  }
  return [fromEng, toEng];
}

var TranslateServer = async function () {
  /** Server that translates GET args. */
  const translate = (words) => {
    /**
     * Builds HTTP response content by using Array.reduce() on split input
     * string then looking up each element in translation dictionaries.
     *
     * @param   {Array<string>} words Query string split using space separator.
     * @returns {string}              Translated phrase.
     */
    try {
      return words[1] != "translate"
        ? "OK"
        : decodeURI(words[3])
            .split(/\+| |%20|\+\+|\+\+\+/) // Incase other encoding types or doublespace.
            .reduce(
              (previous, curr) =>
                `${previous} ${
                  this[words[2]][curr.trim()] // Access by key of this.g2s, this.s2g, etc.
                  || curr // original word if no translation found.
                }`,
              ""
            );
    } catch {
      return "OK";
    }
  };

  // Express App
  const app = express();
  app.use(
    /** Middleware: Express Static Method and CORS headers. */
    express.static("public_html"),
    function (req, res, next) {
      res.header("Access-Control-Allow-Origin", "*");
      res.header(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept"
      );
      next();
    }
  );
  app.get("/", () => {
    console.log("serving index.html");
  });
  app.get("/translate/:translateType/:query", async (req, res) => {
    /**
     * Resolver for translation GET requests.
     * Parsing params using string methods though.
     * @listens Express#request
     */
    res.send(await translate(req.url.toLowerCase().split("/")));
  });
  app.listen(5000, () => {
    /**
     * Server Instance
     * @returns {Server}
     */
    console.log(
      "Listening on port 5000. Allow a second for dictionaries to load :D"
    );
  });
  this.e2g;
  this.g2e;
  this.e2s;
  this.s2e;
  this.g2s = {};
  this.s2g = {};
  [[this.e2g, this.g2e], [this.e2s, this.s2e]] = [
    await mapTranslations(
      "https://benjdd.com/courses/cs337/summer-2021/pas/translate/German.txt"
    ),
    await mapTranslations(
      "https://benjdd.com/courses/cs337/summer-2021/pas/translate/Spanish.txt"
    ),
  ];
  // Create German -> Spanish and vice-versa using intersections of English keys.
  Object.keys(this.e2s)
    .filter((word) => Object.keys(this.e2g).includes(word))
    .forEach((intersection) => {
      this.g2s[this.e2g[intersection]] = this.e2s[intersection];
      this.s2g[this.e2s[intersection]] = this.e2g[intersection];
    });
};

TranslateServer();
