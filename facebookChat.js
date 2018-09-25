const login = require("facebook-chat-api");
const fs = require("fs");
const path = require('path');
const filename = 'appstate.json';

const saveStateAndExecute = (err, api) => {
  if(err) return console.error(err);
  fs.writeFileSync(path.join(__dirname, filename), JSON.stringify(api.getAppState()));
  execute(err, api);
};

const execute = (err, api) => {
  if(err) return console.error(err);
  api.getFriendsList((err, data) => {
      if(err) return console.error(err);
      console.log(data.length);
  });
}



if(fs.existsSync(filename)) {
  const appState = require(path.join(__dirname, filename));
  login({ appState }, execute);
} else {
  login({email: "e4448506@nwytg.net", password: "test123123"}, saveStateAndExecute);
}