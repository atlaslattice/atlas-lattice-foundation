"""
HTAM Fractal Generator v1.0
Variable-Density Constructal Network for Ironwood TPU Cooling Manifold

Author: Gemini (Google) — fractal microfluidics mathematics
Verified: Claude (Anthropic) — code execution + engineering review
Date: April 1, 2026
Sphere: S02 (HTAM Fabrication) — Element 16 (Fractal Cooling Geometries)

Output: 159 segments, 9 generations, min channel 0.79mm (PASS vs 0.5mm floor)
Known issues: half-die coverage, 2D only, no outlet, periphery starvation
"""
import numpy as np
import math

class HTAM_Fractal_Generator:
    def __init__(self, base_depth=6, center_xy=(25.0, 25.0)):
        self.base_depth = base_depth
        self.center_xy = np.array(center_xy)
        self.segments = []
        self.AREA_SCALAR = 2.0 ** (-2.0 / 3.0)
        self.LENGTH_SCALAR = 2.0 ** (-1.0 / 3.0)
        self.BIFURCATION_ANGLE = math.radians(37.47)

    def thermal_density_multiplier(self, x, y):
        distance = np.linalg.norm(np.array([x, y]) - self.center_xy)
        if distance < 10.0:
            return 1.5
        elif distance < 20.0:
            return 1.0
        else:
            return 0.5

    def generalized_murrays_law(self, parent_area, parent_length):
        child_area = parent_area * self.AREA_SCALAR
        child_length = parent_length * self.LENGTH_SCALAR
        return child_area, child_length

    def calculate_bifurcation_angles(self, parent_vector):
        rot_pos = np.array([
            [np.cos(self.BIFURCATION_ANGLE), -np.sin(self.BIFURCATION_ANGLE)],
            [np.sin(self.BIFURCATION_ANGLE),  np.cos(self.BIFURCATION_ANGLE)]
        ])
        rot_neg = np.array([
            [np.cos(-self.BIFURCATION_ANGLE), -np.sin(-self.BIFURCATION_ANGLE)],
            [np.sin(-self.BIFURCATION_ANGLE),  np.cos(-self.BIFURCATION_ANGLE)]
        ])
        return np.dot(rot_pos, parent_vector), np.dot(rot_neg, parent_vector)

    def get_cross_section_shape(self, channel_area):
        width = math.sqrt(channel_area / 0.8)
        height = 0.8 * width
        corner_radius = 0.25 * width
        return width, height, corner_radius

    def generate_constructal_network(self, start_pos, current_vector, current_depth, area, length):
        current_multiplier = self.thermal_density_multiplier(start_pos[0], start_pos[1])
        max_local_depth = int(self.base_depth * current_multiplier)
        if current_depth > max_local_depth:
            return
        norm_vector = current_vector / np.linalg.norm(current_vector)
        end_pos = start_pos + (norm_vector * length)
        width, height, radius = self.get_cross_section_shape(area)
        self.segments.append({
            'generation': current_depth,
            'start_xy': tuple(start_pos),
            'end_xy': tuple(end_pos),
            'area': area,
            'width': width,
            'height': height,
            'corner_radius': radius
        })
        child_area, child_length = self.generalized_murrays_law(area, length)
        vec_left, vec_right = self.calculate_bifurcation_angles(norm_vector)
        self.generate_constructal_network(end_pos, vec_left, current_depth + 1, child_area, child_length)
        self.generate_constructal_network(end_pos, vec_right, current_depth + 1, child_area, child_length)

    def compile_acu_payload(self):
        print(f"[SYSTEM] Compiled Constructal Network: {len(self.segments)} discrete acoustic segments.")
        return self.segments

if __name__ == "__main__":
    generator = HTAM_Fractal_Generator(base_depth=6, center_xy=(25.0, 25.0))
    generator.generate_constructal_network(
        start_pos=np.array([25.0, 0.0]),
        current_vector=np.array([0.0, 1.0]),
        current_depth=1,
        area=20.0,
        length=5.0
    )
    acu_payload = generator.compile_acu_payload()
