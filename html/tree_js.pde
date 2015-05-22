void setup() {
    size(1400, 700);
}

void tree(float trunk, float angle, float trunkscalar, float end_) {
    if (trunk < end_) {
        return;
    }
    line(0, 0, 0, trunk);
    translate(0, trunk);
    pushMatrix();
    rotate(angle);
    tree(trunk*trunkscalar, angle, trunkscalar, end_);
    popMatrix();
    rotate(-angle);
    tree(trunk*trunkscalar, angle, trunkscalar, end_);
}
    
void draw() {
    stroke(0);
    background(255);
    translate(width/2, height);
    scale(1, -1);
    tree(100.0*mouseY/height, 2.0*mouseX/width, .8*mouseY/height, 10);
}

