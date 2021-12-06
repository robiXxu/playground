const { createWorker } = require('tesseract.js');

const worker = createWorker({
  logger: i => console.log(i),
});

const lang = 'eng';

(async() => {
  await worker.load();
  await worker.loadLanguage(lang);
  await worker.initialize(lang);
  const { data: { text } }  = await worker.recognize('https://tesseract.projectnaptha.com/img/eng_bw.png')
  console.log(text);
  await worker.terminate();
})();
