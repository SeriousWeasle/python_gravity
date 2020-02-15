from ws_utils.vec3 import vec3

class cube:
    def __init__(self, pos:vec3, dims:vec3):
        #ground plane
        offset = dims * 0.5
        self.pos = pos
        self.dims = dims
        self.volume = dims.x() * dims.y() * dims.z()

        #ground plane
        self.vtx_a = vec3(pos.x() - offset.x(), pos.y() - offset.y(), pos.z() - offset.z())
        self.vtx_b = vec3(pos.x() + offset.x(), pos.y() - offset.y(), pos.z() - offset.z())
        self.vtx_c = vec3(pos.x() + offset.x(), pos.y() - offset.y(), pos.z() + offset.z())
        self.vtx_d = vec3(pos.x() - offset.x(), pos.y() - offset.y(), pos.z() + offset.z())

        #top plane
        self.vtx_e = vec3(pos.x() - offset.x(), pos.y() + offset.y(), pos.z() - offset.z())
        self.vtx_f = vec3(pos.x() + offset.x(), pos.y() + offset.y(), pos.z() - offset.z())
        self.vtx_g = vec3(pos.x() + offset.x(), pos.y() + offset.y(), pos.z() + offset.z())
        self.vtx_h = vec3(pos.x() - offset.x(), pos.y() + offset.y(), pos.z() + offset.z())

        self.vertices = [self.vtx_a.comps(), self.vtx_b.comps(), self.vtx_c.comps(), self.vtx_d.comps(), self.vtx_e.comps(), self.vtx_f.comps(), self.vtx_g.comps(), self.vtx_h.comps()]

    def getVertices(self):
        return self.vertices
    
    def getVolume(self):
        return self.volume
    
    def getPosition(self):
        return self.pos
    
    def getDimensions(self):
        return self.dims