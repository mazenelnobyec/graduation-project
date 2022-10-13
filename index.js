const express = require('express');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 5000

app.use(cors());
app.use(express.json());


const testRouter = require('./routes/test');

app.use('/test',testRouter)
app.listen(port,() =>{
    console.log(`server is working on port ${port}`)
});