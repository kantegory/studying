var points = [];

var pushPoints = function(x, y, dx, dy) {
  points.push({ x: x, y: y, dx: dx, dy: dy });
};

var buildLine = function(deltaX, deltaY) {
  pushPoints(x, y, deltaX, deltaY);
  x += deltaX;
  y += deltaY;

};

var A = function(level) {
  if (level > 0) {
    A(level - 1);
    buildLine(+dist, +dist);
    B(level - 1);
    buildLine(+2 * dist, 0);
    D(level - 1);
    buildLine(+dist, -dist);
    A(level - 1);
  }
};


var B = function(level) {
  if (level > 0) {
    B(level - 1);
    buildLine(-dist, +dist);
    C(level - 1);
    buildLine(0, +2 * dist);
    A(level - 1);
    buildLine(+dist, +dist);
    B(level - 1);
  }
};

var C = function(level) {
  if (level > 0) {
    C(level - 1);
    buildLine(-dist, -dist);
    D(level - 1);
    buildLine(-2 * dist, 0);
    B(level - 1);
    buildLine(-dist, +dist);
    C(level - 1);
  }
};

var D = function(level) {
  if (level > 0) {
    D(level - 1);
    buildLine(+dist, -dist);
    A(level - 1);
    buildLine(0, -2 * dist);
    C(level - 1);
    buildLine(-dist, -dist);
    D(level - 1);
  }
};


var level = 1;
var dist = 100;

for (var i = level; i > 0; i--) {
  dist = dist / 2;
}

var x = dist * 2;
var y = dist;

var p = 0;
var paint = function() {
  var point = points[p];
  ctx.beginPath();
  ctx.moveTo(point.x, point.y);
  ctx.lineTo(point.x + point.dx, point.y + point.dy);
  ctx.stroke();
  if (p < points.length -1) {
    p++;
    setTimeout(paint, 10);
  }
};




var ctx = document.getElementById('ctx').getContext('2d');
var lvl = document.getElementById('level');
var clear = document.getElementById('clear');
var run = document.getElementById('run');


ctx.lineWidth = 2;
ctx.strokeStyle = 'orange';

clear.addEventListener('click', function() {
  ctx.clearRect(0, 0, 400, 400);
});

run.addEventListener('click', function() {
  level = lvl.value;

  dist = 100;

  for (var i = level; i > 0; i--) {
    dist = dist / 2;
  }

  x = dist * 2;
  y = dist;
  p = 0;


  points = [];

  A(level); // start recursion
  buildLine(+dist, +dist);
  B(level); // start recursion
  buildLine(-dist, +dist);
  C(level); // start recursion
  buildLine(-dist, -dist);
  D(level); // start recursion
  buildLine(+dist, -dist);

  paint();
});
