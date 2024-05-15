const mysql = require('mysql');
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'caomer'
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Conectado ao banco de dados!');
});

app.post('/login', (req, res) => {
  const email = req.body.email;
  const senha = req.body.senha;

  connection.query('SELECT * FROM usuarios WHERE email = ? AND senha = ?', [email, senha], (error, results, fields) => {
    if (error) throw error;

    if (results.length > 0) {
      res.send('Login bem-sucedido!');
    } else {
      res.send('E-mail ou senha incorretos!');
    }
  });
});

app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000');
});
