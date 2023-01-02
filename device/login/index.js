import express from 'express';
import { writeFile } from 'node:fs/promises';
import { check, validationResult } from 'express-validator';

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: true}));

const PORT = 80;
const HOST = '0.0.0.0';

app.use('/', express.static('public'));

app.post('/token', check('token', 'Must specify token').exists(), async (req, res) => {
  const validation = validationResult(req);
  if (!validation.isEmpty()) {
    return res.status(400).json({errors: validation.array()});
  }
  await writeFile('/data/token', req.body.token);
  res.json({success: true});
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Listening on ${HOST}:${PORT}`);
})