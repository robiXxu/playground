const express = require('express');
const app = express();
const port = 8080;

const obj = { prop1: 1, prop2: false, prop3: "test", prop4: (x) => `x=${x}` }

app.use((req,res,next) => {
  req.test = obj;
  next();
});

app.get('/', (req,res) => {
  console.log('/ req.test', req.test);
  req.test.prop1 = 2;
  res.status(200).send("/");
});

app.get('/test', (req,res) => {
  console.log('/test req.test', req.test);
  req.test.prop1 = 3;
  res.status(200).send("/test");
});

app.listen(port, () => {
  console.log(`Listening on ${port}`);
});