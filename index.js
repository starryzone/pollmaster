const express = require('express')
const app = express()
const port = 3000

app.get('/health-hack', (req, res) => {
  res.sendStatus(200)
})

app.post('/health-hack', (req, res) => {
  res.sendStatus(200)
})

app.listen(port, () => {
  console.log(`Health hack listening on port ${port}`)
})
