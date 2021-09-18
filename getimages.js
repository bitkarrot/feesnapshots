const Pageres = require('pageres');

(async () => {
        await new Pageres({delay: 2})
        .src('https://jochen-hoenicke.de/queue/#BTC,24h,fee', ['1280x1024'], {filename: 'johoe_24h', crop: true})
        .src('https://whatthefee.io/', ['1024x768'], {selector: 'table.FeeTable', filename: 'wtf', crop: true})
                .dest('./images')
                .run();

        console.log('Finished generating screenshots!');
})();
