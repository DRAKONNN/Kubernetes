const express = require('express');
const app = express();
const fs = require('fs');
const movies = JSON.parse(fs.readFileSync('movies.json'));

app.get('/movies', (req, res) => {
  res.json(movies);
});

app.get('/', (req, res) => {
  res.send('<h1>Blockbuster App</h1><p>Use <a href="/movies">/movies</a> to see the list.</p>');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Blockbuster running on port ${PORT}`);
});
