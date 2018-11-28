const querystring = require('querystring');

const url = "http://example.com/?product=shirt&color=blue&newuser&size=m"



// encodeURIComponent(url); in js
const encodeURIComponentJS = "http%3A%2F%2Fexample.com%2F%3Fproduct%3Dshirt%26color%3Dblue%26newuser%26size%3Dm";

const querystringEncode = querystring.escape(url);

const encodeURIComponentNode = encodeURIComponent(url);

const encodeURINode = encodeURI(url);

console.log('encodeURIComponentJS', encodeURIComponentJS);
console.log('querystringEncode', querystringEncode);
console.log('encodeURIComponentNode', encodeURIComponentNode);

console.log('encodeURINode', encodeURINode);
