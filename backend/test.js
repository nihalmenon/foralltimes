const fetchOneByKey = require('./read')

const f = async () => {
    try {
        const ans = await fetchOneByKey()
        console.log(ans)
    } catch(e) {
        console.log(e)
    }
    
}

f()


