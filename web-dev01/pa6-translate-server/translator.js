/**
 * PA6 | CSC337 Summer 2021
 *
 * Http server that responds to requests by translating query params
 * and sending translated words in response.
 * Test w/ URL list:
 * node . & xargs -a __urls__.txt -i google-chrome --new-tab http://127.0.0.1:5000/translate/{}
 *
 * @author Christian P. Byrne
 *
 *
 */

const fetch = require("node-fetch");
const http = require("http");

// type Translations = {
//   [startWord: string]: string;
// };
// type MirrorTranslations = Promise<[fromEng: Translations, toEng: Translations]>;

async function mapTranslations(url) {
  /**
   * Fetches text data from benjdd.com translation dictionary files.
   *
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
  var toEng = {};
  var fromEng = {};
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
  /**
   * Main. Void. Server that translates query args.
   *
   * Fetches then maps translation objects. Parse URL path to determine
   * correct dictionary. Respond with translations.
   */
  const translate = (words) => {
    /**
     * Builds HTTP response content by using Array.reduce() and dictionary
     * lookups on array of space-separated query words.
     *
     * @param   {Array<string>} words Query string split using '+' separator.
     * @returns {string}              Translated phrase.
     */
    return words[1] != "translate"
      ? "OK"
      : words[3].split("+").reduce(
          (previous, curr) =>
            `${previous} ${
              this[words[2]][curr] // Access by key of this.g2s, this.s2g, etc.
              || curr // original word if no translation found
            }`,
          ""
        );
  };

  http
    .createServer(async (req, res) => {
      /**
       * http Server Instance
       * @listens http.Server#request
       */
      res.end(await translate(req.url.toLowerCase().split("/")));
    })
    .listen(5000);

  [[this.e2g, this.g2e], [this.e2s, this.s2e]] = [
    await mapTranslations(
      "https://benjdd.com/courses/cs337/summer-2021/pas/translate/German.txt"
    ),
    await mapTranslations(
      "https://benjdd.com/courses/cs337/summer-2021/pas/translate/Spanish.txt"
    ),
  ];
  this.g2s = {};
  this.s2g = {};
  // Create germain -> spanish and vice-versa using intersections of English keys.
  Object.keys(e2s)
    .filter((word) => Object.keys(e2g).includes(word))
    .forEach((intersection) => {
      g2s[e2g[intersection]] = e2s[intersection];
      s2g[e2s[intersection]] = e2g[intersection];
    });
};

TranslateServer();
