const express = require('express');
const redis = require('redis');

const app = express();
const client = redis.createClient({
    url: 'redis://redis:6379'
});

client.on('error', (err) => console.log('Redis Client Error', err));

async function startApp() {
    await client.connect();

    app.get('/', async (req, res) => {
        const visits = await client.incr('visits');
        res.send(`<h1>Hello from Docker Compose!</h1><p>Visitor count: ${visits}</p>`);
    });

    app.listen(3000, () => {
        console.log('Server is running on port 3000');
    });
}

startApp();
