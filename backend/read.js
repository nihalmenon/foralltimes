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

module.exports = getData