const AWS = require('aws-sdk')
const getData = require('./read')

const awsConfig = {
    "region": "us-east-2",
    "endpoint": "dynamodb.us-east-2.amazonaws.com",
    "accessKeyId": "AKIAY3JD2P25DDKKG5H4",
    "secretAccessKey": "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"
}

AWS.config.update(awsConfig)

const dynamoDB = new AWS.DynamoDB.DocumentClient()


const updateOne = (async (change) => {
    try {
        const item = await getData()
        console.log(item)
        const counter = item.counter
    } catch (e) {
        process.exit(1)
    }
    
    const params = {
        TableName: 'foralltimesDB',
        Key: {
            "id": 1
        },
        UpdateExpression: 'set counter = :counter',
        ExpressionAttributeValues: {
            ':counter': counter + change
        }
    }

    try {
        await dynamoDB.update(params, (error, data) => {
            if(error) {
                console.log("error: " + JSON.stringify(error, null, ))
            }else{
                console.log(JSON.stringify(data,null,2));
            }
        })
    } catch (e) {
        console.log('error: ' + e)
    }
    
})().catch( e => { console.error(e) })

// module.exports = updateOne