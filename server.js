const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const ejs = require('ejs')
let Patient = require('./models/patient.model');
let Stats = require('./models/stats.model');


async function listDatabase(client){
    database = await client.db().admin().listDatabases();
    console.log("Databases:");
    databasesList.databases.forEach(db => console.log(` - ${db.name}`));
}


require('dotenv').config();

const app = express();
const port = process.env.PORT || 8080
app.set('view engine','ejs')

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended:false}))
const uri = process.env.ATLAS_URI;
mongoose.connect(uri,{useNewUrlParser:true, useCreateIndex:true,useUnifiedTopology:true});

const connection =  mongoose.connection;
connection.once('open',() => {
    console.log('Db connected successfully');   

});


const patientsContainer = require('./routes/patient');
const { json } = require('express');
//let patitentsData = patientsContainer.patientData;
let patient;

app.get('/stats',async function(req,res){
    let grabber = await Stats.find();

    res.send(grabber)
    
})

app.get('/', async function(req, res) {
    
  /*  Patient.find()
    .then(patients => res.json(patients))
    .catch(err => res.status(400).json('Error: '+err));
   */
    let grabber =  await   Patient.find();

    // console.log(grabber[0])
    // console.log(grabber[0].bed_number)
    // console.log(typeof(grabber[0]))
    obj = grabber[0]
    let length = grabber.length
    if (grabber.length == 0)
        res.send('No Cases attatched')
    res.render('ui',{obj,length});
    
});

app.get('/edit',(req,res) =>{
    res.sendFile(__dirname+'/static/manage_data.html')
});

app.post('/edit', async (req,res) =>{
    let patientname = req.body.patientname;
    let enteringdata = req.body.enteringdata;
    console.log(`entering date: ${enteringdata} patient name: ${patientname}`);
    let grabber =  await   Patient.findOneAndUpdate({},{name:patientname,arrival_data:enteringdata})
    res.sendFile(__dirname+'/static/redirect.html')
    
})


app.listen(port,() =>{
    console.log(`server is working on port ${port}`)
});