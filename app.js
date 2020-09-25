var express = require("express");
var bodyParser = require("body-parser");
var multer = require('multer');
var app = express();

app.use(bodyParser.json());

var storage = multer.diskStorage({
  destination: function (req, file, callback) {
    callback(null, './uploads');
  },
  filename: function (req, file, callback) {
    callback(null, file.fieldname + Math.random() + '-' + Date.now() + '.jpg');
  }
});

app.post('/api/photo',function(req,res){
    console.log(Number(req.query.numFiles), typeof(Number(req.query.numFiles)))
    // req.query.paramName - this has the number of files set

    var upload = multer({ storage : storage }).array('userPhoto', Number(req.query.numFiles));
    upload(req,res,function(err) {
        if(err) {
            console.log(err)
            return res.end("Error uploading file.");
        }
        res.end("File is uploaded");
    });
});

app.listen(3000,function(){
    console.log("Working on port 3000");
});