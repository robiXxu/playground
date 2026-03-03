

const someFn = () => {
  // F(find backward) b(char)
  // c(hange)b(backward)
  // A(ppend - uppercase = at the end of the line)
  // --
  // A(ppend)
  // _(underscore - goes to first char
  // c(hange)w(ord)
  // --
  // 4b(jumps backward 4 times)
  // c(hange)w(ord)
  // A(ppend)
  const button = document.createElement('button');

  button.innerText = 'this button does something very special';
  button.setAttribute('something', 'value');

  button.onclick = () => window.location = 'https://youtu.be/dQw4w9WgXcQ';

  document.body.append(button);
}
