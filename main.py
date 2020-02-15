from ws_utils.vec2 import vec2
import ws_utils.particles as particles
from tqdm import tqdm
settings = {
    "attraction_falloff_exponent": 2,
    "repulsion_falloff_exponent": 4,
    "width": 256,
    "height": 256,
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
            "count": 20
        },
        "C": {
            "mass": 3e11,
            "color": [0, 0, 255],
            "count": 1
        }
    }
}

scene = particles.scene(settings)
for i in tqdm(range(1000), desc="Rendering frames"):
    scene.render()
    scene.tick()