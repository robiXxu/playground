const { spawn } = require('child_process');

const whois = spawn('whois',['saveni.ro']);

whois.stdout.on('data', (data) => {
  const regex = /^(\s)+([a-zA-Z\s])+(:)(\s)([a-zA-Z0-9]|[:/\.-])+/gm;
  console.log(`stdout: ${data.toString().match(regex)}`);
});

whois.stderr.on('data', (data) => {
  
  console.log(`stderr: ${data}`);
});

whois.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});