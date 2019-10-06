Array.prototype.random = function() { return this[Math.floor((Math.random()*this.length))]; };

var Point = function (x, y) {
  this.x = x;
  this.y = y;
};

Point.prototype.distance = function (other) {
  return new Point(
    this.x - other.x,
    this.y - other.y
  );
};

Point.prototype.halfway = function (other) {
  var distance = this.distance(other);
  return new Point(
    this.x - (distance.x / 2),
    this.y - (distance.y / 2)
  );
};

var Sierpinski = function (id) {
  this.canvas = document.getElementById(id) || document.getElementsByTagName("canvas")[0];
  this.x_size = this.canvas.width;
  this.y_size = this.canvas.height;
  this.points = [
    new Point(this.x_size/2, 0),
    new Point(0, this.x_size * Math.cos(Math.PI / 6)),
    new Point(this.x_size, this.x_size * Math.cos(Math.PI / 6))
  ];
  this.current_point = new Point(
    Math.floor((Math.random() * this.x_size)),
    Math.floor((Math.random() * this.y_size))
  );
  this.canvas = this.canvas.getContext("2d");
  for (var i = 0; i < this.points.length; i++) {
    this.draw_point(this.points[i]);
  }
};

Sierpinski.prototype.draw = function () {
  var midpoint = this.current_point.halfway(this.points.random());
  this.draw_point(midpoint);
  this.current_point = midpoint;
};

Sierpinski.prototype.draw_point = function (point) {
  var c = this.canvas;
  c.fillStyle = "#000000";
  c.beginPath();
  c.arc(point.x, point.y, 1, 0, Math.PI * 2, true);
  c.closePath();
  c.fill();
};
