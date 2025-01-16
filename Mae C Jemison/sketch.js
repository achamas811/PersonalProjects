let backdrop;

function preload(){
  backdrop = loadImage('C:/Users/alexa/Downloads/space.jpg');
}
function setup() {
  createCanvas(windowWidth, windowHeight);
  
}
function draw(){
  background(backdrop);
  fill(255, 255, 255);
}
