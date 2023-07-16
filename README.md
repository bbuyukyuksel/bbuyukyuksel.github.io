# Flexible-Jekyll is a simple and clean theme for Jekyll

## Features

- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](http://fontawesome.io/)
- [Disqus](https://disqus.com/)
- [Analytics](https://analytics.google.com/analytics/web/)
- Support Emoji

## Installation:

Fork the ``master`` branch and follow the [Jekyll Installation Documentation](https://jekyllrb.com/docs/installation/).

- For running
  
  ```shell
  bundle exec jeykll server
  ```

## Creating Contents:

```javascript
let items = document.querySelectorAll("h1, h2, h3, h4, h5, h6");

let content = "";

for(let i=2; i<items.length - 2; ++i){
    content += `- '${items[i].textContent};${items[i].id}'\n`;
}

console.log(content);
```

## License

GNU General Public License v3.0
