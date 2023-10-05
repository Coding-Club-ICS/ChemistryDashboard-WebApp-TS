const cors = require('cors');
const express = require('express');
const balancer = require('@akikowo/chemical-balancer')

const app = express();

app.use(cors());

app.get('/chem/balance/:equation', (req, res) => {
    res.send(balancer.balance(req.params.equation));
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

app.listen(3000, () => {
    console.log('Listening on port 3000');
});