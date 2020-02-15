def mapRange(value, lv, hv, minv, maxv):
    return (((value - lv)/(hv-lv))*(maxv-minv)) + minv