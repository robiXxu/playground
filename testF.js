
var search = [
  {
    value: 'Laptop Kiano SlimNote 14.2 HDD cu procesor Intel® Celeron® N3350',
    property: 'title'
  }
]

var data = {};
search.forEach(s => {
  const els = Array.from(document.all).filter(el => el.textContent.includes(s.value))
  const el = els[els.length - 1];

    const elements = (el.id.trim().length > 0) ? 
      document.querySelectorAll(`${el.tagName}#${el.id}`) :
      document.querySelectorAll(`${el.tagName}.${el.className}`);

    Array.from(elements).forEach((e,i) => { 
      const key = s.property;
      if(data[i])
        data[i][key] = e.textContent.trim();
    })
  
})
