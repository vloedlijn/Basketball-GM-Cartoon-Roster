// runBuildSVGString.js
const { buildSVGString } = require('../../facesjs');

process.stdin.setEncoding('utf8');

let data = '';

process.stdin.on('readable', () => {
  let chunk;
  while ((chunk = process.stdin.read()) !== null) {
    data += chunk;
  }
});

process.stdin.on('end', () => {
  const playerData = JSON.parse(data);
  const svgString = buildSVGString(playerData);
  process.stdout.write(svgString);
});
