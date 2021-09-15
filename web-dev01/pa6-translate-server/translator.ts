import fetch from "node-fetch";
import { createServer } from "http";

type Translations = {
  [startWord: string]: string;
};
type MirrorTranslations = [fromEng: Translations, toEng: Translations];

async function mapTranslations(url: string): Promise<MirrorTranslations> {
  return fetch(url)
    .then((response) => response.text())
    .then(async (text) => {
      return await jsonifyRes(text);
    });
}

function jsonifyRes(text: string): MirrorTranslations {
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
  const translate = (words: Array<string>) => {
    return words[1] != "translate"
      ? "OK"
      : words[3]
          .split("+")
          .reduce(
            (previous, curr) => `${previous} ${this[words[2]][curr] || curr}`,
            ""
          );
  };

  createServer(async (req, res) => {
    const parsed: Array<string> = req.url.toLowerCase().split("/");
    res.end(await translate(parsed));
  }).listen(5000);

  [[this.e2g, this.g2e], [this.e2s, this.s2e]] = [
    await mapTranslations(
      "https://benjdd.com/courses/cs337/summer-2021/pas/translate/German.txt"
    ),
    await mapTranslations(
      "https://benjdd.com/courses/cs337/summer-2021/pas/translate/Spanish.txt"
    ),
  ];
  this.g2s as Translations;
  this.s2g as Translations;
  Object.keys(this.e2s)
    .filter((word) => Object.keys(this.e2g).includes(word))
    .forEach((intersection) => {
      this.g2s[this.e2g[intersection]] = this.e2s[intersection];
      this.s2g[this.e2s[intersection]] = this.e2g[intersection];
    });
};

TranslateServer();
