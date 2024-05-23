#!/usr/bin/node
 /**
  * Star Wars Characters
*/


const request = require('request');

const lastArg = process.argv[process.argv.length - 1];
const urlFilm = "https://swapi-api.alx-tools.com/api/films/" + lastArg;

const makeRequest = (url) => {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode !== 200) {
                reject(new Error('Failed to load page, status code: ' + response.statusCode));
            } else {
                resolve(JSON.parse(body));
            }
        });
    });
};

const fetchFilm = () => {
    return makeRequest(urlFilm)
        .then(data => data['characters']);
};

const fetchChar = () => {
    return fetchFilm()
        .then(urls => {
            if (!urls) {
                throw new Error('No URLs found');
            }
            const charPromises = urls.map(url => makeRequest(url).then(character => character['name']));
            return Promise.all(charPromises);
        });
};


const main = async () => {
  try {
    const characters = await fetchChar();

    for (const character of characters) {
      console.log(character);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
