const AWS = require('aws-sdk')

// New ID key

const awsConfig = {
    "region": "",
    "endpoint": "",
    "accessKeyId": ""
}
AWS.config.update(awsConfig)

const dynamoDB = new AWS.DynamoDB.DocumentClient()

const fetchOneByKey = () => {
    const params = {
        TableName: '',
        Key: {
            "id": ""
        }
    }
    try {
        docClient.get(params, (error, data) => {
            if(error) {
                console.log("error: " + JSON.stringify(error, null, ))
            }else{
                console.log(JSON.stringify(data,null,2));
            }
        })
    } catch (e) {
        console.log('error: ' + e)
    }
    
}