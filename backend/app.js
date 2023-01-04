const path = require('path')
const express = require('express')
const hbs = require('hbs')
const moment = require('moment')


// const getData = require('./read')

const app = express()
const port = process.env.PORT || 3000

// Define paths for Express config
const publicDirectoryPath = path.join(__dirname, '../public')
const viewsPath = path.join(__dirname, '../templates/views')
const partialsPath = path.join(__dirname, '../templates/partials')


// Setup handlebars engine and views location
app.set('view engine', 'hbs')
app.set('views', viewsPath)
hbs.registerPartials(partialsPath)

// Setup static directory to serve
app.use(express.static(publicDirectoryPath))

const AWS = require('aws-sdk')

const awsConfig = {
    "region": "us-east-2",
    "endpoint": "dynamodb.us-east-2.amazonaws.com",
    "accessKeyId": "AKIAY3JD2P25DDKKG5H4",
    "secretAccessKey": "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"
}
AWS.config.update(awsConfig)

const dynamoDB = new AWS.DynamoDB.DocumentClient()

const fetchOneByKey = async () => {
    const params = {
        TableName: 'foralltimesDB',
        Key: {
            "id": 1
        }
    }
    try {
        const data = await dynamoDB.get(params).promise()
        const item = data.Item
        return {counter: item.counter, time: item.time}
    } catch (e) {
        console.log('error: ' + e)
        return e
    }
    
}


const getData = async () => {
    try {
        const item = await fetchOneByKey()
        return {counter: item.counter, time: item.time}
    } catch (e) {
        return e
    }
}

moment.tz.setDefault("America/New_York");

app.get('', async (req, res) => {
    const data = await getData()

    res.render('index', {
        counter: data.counter,
        time: moment().format('h:mm a')
    })
})

app.listen(port, () => {
    console.log('Server is up on port ' + port)
})