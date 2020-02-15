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
            for c in range(ptype["count"]):
                pa.append(particle(vec2(random.random()*self.w, random.random()*self.h), vec2(random.uniform(-3, 3), random.uniform(-3, 3)), ptype["mass"], ptype["color"]))
            #add particle array to scene particles
            self.particles[t] = pa
    
    def render(self):
        frame = Image.new("RGB", (self.w, self.h), "black")
        pixels = frame.load()
        for t in self.particles:
            for p in self.particles[t]:
                px = int(p.pv.x())
                py = int(p.pv.y())
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
        frame.save(str(self.fc) + ".png")
        self.fc += 1

    def tick(self):
        newptc = {}
        for t in self.particles:
            npa = []
            for p in self.particles[t]:
                fv = vec2(0, 0)
                for rt in self.particles:
                    for rp in self.particles[rt]:
                        if p != rp:
                            av = ((self.bg * p.m * rp.m)/((p.pv - rp.pv).length()*(p.pv - rp.pv).length()))*(p.pv - rp.pv)
                            fv = fv + av
                p.vv = p.vv + fv
                p.pv = p.pv + p.vv
                if p.pv.x() >= self.w:
                    p.pv = vec2(self.w - (p.pv.x() - self.w), p.pv.y())
                    p.vv = vec2(p.vv.x() * -1, p.vv.y())
                if p.pv.x() <= 0:
                    p.pv = vec2(p.pv.x() * -1, p.pv.y())
                    p.vv = vec2(p.vv.x() * -1, p.vv.y())
                
                if p.pv.y() >= self.h:
                    p.pv = vec2(p.pv.x(), self.h - (p.pv.y() - self.h))
                    p.vv = vec2(p.vv.x(), p.vv.y() * -1)
                if p.pv.y() <= 0:
                    p.pv = vec2(p.pv.x(), p.pv.y() * -1)
                    p.vv = vec2(p.vv.x(), p.vv.y() * -1)
                npa.append(p)
            newptc[t] = npa
        self.particles = newptc