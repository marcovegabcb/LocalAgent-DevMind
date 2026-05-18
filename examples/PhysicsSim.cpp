#include <iostream>
#include <vector>

struct Vector2D {
    float x, y;
};

class Particle {
public:
    Vector2D position;
    Vector2D velocity;

    void update(float deltaTime) {
        position.x += velocity.x * deltaTime;
        position.y += velocity.y * deltaTime;
    }
};

int main() {
    Particle p = {{0, 0}, {10, 5}};
    float timeStep = 0.1f;

    for(int i = 0; i < 5; i++) {
        p.update(timeStep);
        std::cout << "Punto " << i << ": (" << p.position.x << ", " << p.position.y << ")" << std::endl;
    }
    return 0;
}
