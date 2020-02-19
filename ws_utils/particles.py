import math
from PIL import Image
import random
from ws_utils.vec2 import vec2

class particle:
    def __init__(self, pos:vec2, vel:vec2, mass:float, color:tuple):
        self.pv = pos
        self.vv = vel
        self.m = mass
        self.c = color

class scene:
    def __init__(self, settings):
        #set settings from main.py in handler
        self.fe = settings["attraction_falloff_exponent"]
        self.w = settings["width"]
        self.h = settings["height"]
        self.bg = settings["bigg"]
        self.frames = []
        self.fc = 0
        #make empty object to store particles in
        self.particles = {}

        #get particle types from settings
        ptypes = settings["particles"]
        
        #loop over each type
        for t in ptypes:
            #particle array for type
            pa = []
            ptype = ptypes[t]
            #add specified amount of particles
            if t == "C":
                    pa.append(particle(vec2(self.w/2, self.h/2), vec2(random.uniform(0, 0), random.uniform(0, 0)), ptype["mass"], ptype["color"]))
            else:
                for c in range(ptype["count"]):
                    pa.append(particle(vec2(random.random()*self.w, random.random()*self.h), vec2(random.uniform(-1, 1), random.uniform(-1, 1)), ptype["mass"], ptype["color"]))
            #add particle array to scene particles
            self.particles[t] = pa
    
    def render(self):
        frame = Image.new("RGB", (self.w, self.h), "black")
        pixels = frame.load()
        for t in self.particles:
            for p in self.particles[t]:
                px = int(p.pv.x())
                py = int(p.pv.y())
                if px > 0 and px < self.w and py > 0 and py < self.h:
                    cr, cg, cb = pixels[px, py]
                    pr, pg, pb = p.c
                    nr = cr + pr
                    ng = cg + pg
                    nb = cb + pb
                    if nr > 255:
                        nr = 255
                    if ng > 255:
                        ng = 255
                    if nb > 255:
                        nb = 255
                    pixels[px, py] = (nr, ng, nb)
        self.frames.append(frame)
        frame.save("./frames/" + str(self.fc) + ".png")
        self.fc += 1

    def exportFrames(self):
        self.frames[0].save("test.gif", format="GIF", append_images=self.frames[1:], save_all=True, duration=1, loop=0)

    def tick(self):
        newptc = {}
        for t in self.particles:
            npa = []
            for p in self.particles[t]:
                av = vec2(0, 0)
                for rt in self.particles:
                    for rp in self.particles[rt]:
                        if p != rp:
                            force = (self.bg * p.m * rp.m) / ((p.pv - rp.pv).length() * (p.pv - rp.pv).length())
                            accel = force / p.m
                            xscale = (p.pv - rp.pv).x() / (p.pv - rp.pv).length()
                            yscale = (p.pv - rp.pv).y() / (p.pv - rp.pv).length()
                            av = av + vec2((accel*xscale), (accel*yscale))
                p.vv = p.vv + av
                p.pv = p.pv + p.vv
                # if p.pv.x() >= self.w:
                #     p.pv = vec2(self.w - (p.pv.x() - self.w), p.pv.y())
                #     p.vv = vec2(p.vv.x() * -1, p.vv.y())
                # if p.pv.x() <= 0:
                #     p.pv = vec2(p.pv.x() * -1, p.pv.y())
                #     p.vv = vec2(p.vv.x() * -1, p.vv.y())
                
                # if p.pv.y() >= self.h:
                #     p.pv = vec2(p.pv.x(), self.h - (p.pv.y() - self.h))
                #     p.vv = vec2(p.vv.x(), p.vv.y() * -1)
                # if p.pv.y() <= 0:
                #     p.pv = vec2(p.pv.x(), p.pv.y() * -1)
                #     p.vv = vec2(p.vv.x(), p.vv.y() * -1)
                npa.append(p)
            newptc[t] = npa
        self.particles = newptc