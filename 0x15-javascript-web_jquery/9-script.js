$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
  const helloTranslation = data.hello;
  $('DIV#hello').text(helloTranslation);
});
