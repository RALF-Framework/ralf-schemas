import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';
import YAML from 'yaml';

const root = process.cwd();
const schemaDir = path.join(root, 'schemas', 'draft', '2020-12');
const manifestPath = path.join(root, 'tests', 'validation-manifest.yaml');

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

function readData(file) {
  const text = fs.readFileSync(file, 'utf8');
  if (file.endsWith('.yaml') || file.endsWith('.yml')) return YAML.parse(text);
  return JSON.parse(text);
}

const ajv = new Ajv2020({ allErrors: true, strict: false });
addFormats(ajv);

for (const file of fs.readdirSync(schemaDir)) {
  if (file.endsWith('.schema.json')) ajv.addSchema(readJson(path.join(schemaDir, file)));
}

const manifest = YAML.parse(fs.readFileSync(manifestPath, 'utf8'));
let ok = true;

for (const [expectation, shouldPass] of [['valid', true], ['invalid', false]]) {
  for (const item of manifest[expectation] ?? []) {
    const schema = readJson(path.join(root, item.schema));
    const validate = ajv.getSchema(schema.$id) || ajv.compile(schema);
    const data = readData(path.join(root, item.file));
    const passed = validate(data);
    if (passed === shouldPass) {
      console.log(`PASS ${item.file}`);
    } else {
      ok = false;
      console.log(`FAIL ${item.file}`);
      console.log(validate.errors);
    }
  }
}

process.exit(ok ? 0 : 1);
