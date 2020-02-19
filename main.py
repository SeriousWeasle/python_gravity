from ws_utils.vec2 import vec2
import ws_utils.particles as particles
from tqdm import tqdm
settings = {
    "attraction_falloff_exponent": 2,
    "repulsion_falloff_exponent": 4,
    "width": 2048,
    "height": 2048,
    "bigg": -6.7e-11,
    "particles": {
        "A": {
            "mass": 1,
            "color": [255, 0, 0],
            "count": 40
        },
        "B": {
            "mass": 0.6,
            "color": [0, 255, 0],
            "count": 150
        },
        "C": {
            "mass": 3e11,
            "color": [0, 0, 255],
            "count": 1
        },
        "D": {
            "mass": 5000,
            "color": [255, 255, 0],
            "count": 24
        },
        "E": {
            "mass": 0.01,
            "color": [0, 255, 255],
            "count": 500
        },
        "F": {
            "mass": 300,
            "color": [255, 0, 255],
            "count": 16
        },
        "G": {
            "mass": 17,
            "color": [127, 0, 255],
            "count": 50
        },
        "H": {
            "mass": 8e6,
            "color": [127, 0, 255],
            "count": 4
        }
    }
}

scene = particles.scene(settings)
for i in tqdm(range(25000), desc="Rendering frames"):
    scene.render()
    scene.tick()
print("Making GIF, this may take a while depending on frame size and count")
scene.exportFrames()
print("Done.")