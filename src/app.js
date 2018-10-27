import {Application, Graphics} from 'PIXI.js';
import {PythonShell} from 'python-shell';;


const app = new Application({
    autoResize: true,
    resolution: devicePixelRatio
});

const graphics = new Graphics();
const multiplier = 6;
let metadata, world;

let pyshell = new PythonShell('my_script.py', {mode: "json"});

pyshell.on('message', function (message) {
    console.log(message);
    metadata = message['metadata'];
    world = message['world']
});

pyshell.end(function (err,code,signal) {
    if (err) throw err;

    for (let x=0; x < metadata['width']; x++) {
        for (let y=0; y < metadata['height']; y++) {
            graphics.beginFill(parseInt(world[x][y]["color"], 16));
            graphics.drawRect(x*multiplier, y*multiplier, multiplier, multiplier);
            graphics.endFill()
        }
    }

    app.stage.addChild(graphics);
});

window.addEventListener('resize', resize);

function resize() {
    app.renderer.resize(window.innerWidth, window.innerHeight);
}

resize();

document.body.appendChild(app.view);