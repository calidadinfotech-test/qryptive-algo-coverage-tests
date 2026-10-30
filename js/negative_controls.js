// Ordinary code that only LOOKS like cryptography. A correct scanner reports nothing here.
// TODO: replace RSA with ML-KEM and stop using MD5 for cache keys
/* const legacy = crypto.createCipheriv('des-ede3-cbc', key, iv); */

const seedData = [{ name: 'present' }, { name: 'rainbow' }, { name: 'cross' }];
const teaMenu = ['green', 'black'];
const ariaLabel = 'Close dialog';
const aesthetic = 'minimal';

function renderButton(label) {
  return `<button aria-label="${ariaLabel}">${label}</button>`;
}

function opaqueColour(alpha) {
  return `rgba(0, 0, 0, ${alpha})`;
}

function bikeRoute(points) {
  return points.map((p) => ({ lat: p.lat, lng: p.lng }));
}

console.log('present', seedData.length, teaMenu.length, aesthetic);

module.exports = { renderButton, opaqueColour, bikeRoute };
