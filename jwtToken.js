const jwt = require('jsonwebtoken');
const jws = require('jws');

const payload = {"something":"something"};

const config = {
  "header-name": "Authorization",
  "secret": "something",
  "algo": "HS256",
  "type": "JWT"
}

const token2 = jwt.sign(payload, config.secret, {
  header: {
    "typ": config.type,
    "typ": config.algo
  }
});

const token = jws.sign({
  header: {
    "typ": config.type,
    "alg": config.algo
  },
  payload,
  secret: config.secret
});


console.log(token);

console.log(token2)

