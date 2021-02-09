import math

class Color():
    r = 0;
    g = 0;
    b = 0;
    
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def cosine_interpolate(y1, y2, mu):
        mu2 = (1 - math.cos(mu * math.pi)) / 2
        return y1 * (1 - mu2) + y2 * mu2
    
    def linear_interpolate(y1, y2, mu):
        return y1 * (1 - mu) + y2 * mu;

    def interpolate(colors, ratio, interpolation_type):
        length = len(colors)
        i = 1
        total_distance = 0
        while i < length:
            color_b = colors[i]
            color_a = colors[i - 1]
            total_distance += 1#math.sqrt((color_b.r - color_a.r) ** 2 + (color_b.g - color_a.g) ** 2 + (color_b.b - color_a.b) ** 2)
            i += 1

        target_distance = ratio * total_distance
        i = 1
        curr_distance = 0
        prev_distance = 0
        start_index = -1
        while i < length:
            prev_distance = curr_distance
            color_b = colors[i]
            color_a = colors[i - 1]
            curr_distance += 1#math.sqrt((color_b.r - color_a.r) ** 2 + (color_b.g - color_a.g) ** 2 + (color_b.b - color_a.b) ** 2)
            if curr_distance >= target_distance:
                start_index = i - 1
                break
            i += 1
        
        
        conversion_ratio = (target_distance - prev_distance) / (curr_distance - prev_distance)
        new_r = 0
        new_g = 0
        new_b = 0
        if interpolation_type == "cosine":
            new_r = Color.cosine_interpolate(colors[start_index].r, colors[start_index + 1].r, conversion_ratio)
            new_g = Color.cosine_interpolate(colors[start_index].g, colors[start_index + 1].g, conversion_ratio)
            new_b = Color.cosine_interpolate(colors[start_index].b, colors[start_index + 1].b, conversion_ratio)
        else:
            new_r = Color.linear_interpolate(colors[start_index].r, colors[start_index + 1].r, conversion_ratio)
            new_g = Color.linear_interpolate(colors[start_index].g, colors[start_index + 1].g, conversion_ratio)
            new_b = Color.linear_interpolate(colors[start_index].b, colors[start_index + 1].b, conversion_ratio)
                        
        return Color(new_r, new_g, new_b)
        

        
        
