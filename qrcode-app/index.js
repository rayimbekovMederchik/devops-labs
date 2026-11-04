const QRCode = require('qrcode');

const text = process.env.QR_TEXT || 'Hello from DevOps LAB 3!';

QRCode.toString(text, {type: 'terminal'}, (err, url) => {
	if (err) throw err;
console.log(url);
});


