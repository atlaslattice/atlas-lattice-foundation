"""
HTAM Fractal Cooling Manifold Generator v1.1 (MERGED)

Atlas Lattice Foundation — Memphis Node Zero
Operation: Trashium Cooling Blues

Author: Gemini (Google) — fractal vector math, Murray's Law implementation,
        fluid dynamics optimizations, bifurcation angle calculations
Integration: Claude (Anthropic) — spec alignment, documentation, GitHub packaging
Validation: DeepSeek — acoustic overhang analysis (PENDING)

This is the fully integrated logic engine that takes a thermal map (Ironwood TPU
or any heat source) and generates the 3D voxel parameters for the Acoustic
Control Unit (ACU).

Mathematical Basis:
  - Murray's Law (1926): r_p^3 = r_d1^3 + r_d2^3
  - Generalized Murray's Law for non-circular cross-sections:
      A_(i+1) = A_i * 2^(-2/3)
      L_(i+1) = L_i * 2^(-1/3)
  - Optimal Symmetric Bifurcation Angle: +/-37.47 deg (minimizes pumping power)
  - Variable-Density Constructal Network (Bejan, 1997; adapted by Gemini)

Version History:
  v1.0 (2026-03-29) — Skeleton with Murray's Law scaling and thermal density
                       multiplier. TODOs for vector math and cross-sections.
  v1.1 (2026-03-29) — MERGED: Gemini's bifurcation angle calculations (37.47 deg),
                       rounded-square cross-section geometry, full recursive
                       vector math replacing all TODOs. Ready for ACU simulation.

Status: v1.1 — READY FOR ACU SIMULATION

Parent Spec: docs/Memphis_Pilot_Spec_v1.0.md
HTAM Spec: docs/Holographic_Trashium_Acoustic_Spec_v1.0.md (v1.1)

Repository: https://github.com/atlaslattice/atlas-lattice-foundation
"""

import numpy as np


class HTAM_Fractal_Generator:
    """
    Generates a Variable-Density Constructal Network for micro-fluidic
    cooling manifolds, optimized for HTAM acoustic standing wave fabrication.

    The fractal branching follows Generalized Murray's Law for non-circular
    (rectangular/trapezoidal) cross-sections — the natural geometry produced
    by acoustic pressure-node confinement against a flat basin floor.

    v1.1 additions (Gemini):
      - calculate_bifurcation_angles(): +/-37.47 deg optimal Murray deviation
      - get_cross_section_shape(): Rounded squares for max thermal contact
      - Full recursive vector math in generate_constructal_network()
    """

    def __init__(self, die_size=(50, 50), base_radius=2.5, max_depth=6):
        """
        Args:
            die_size: (width_mm, height_mm) of the target thermal surface
            base_radius: Inlet channel radius in mm
            max_depth: Maximum branching generations for the fractal network
        """
        self.die_size = die_size  # mm
        self.base_radius = base_radius  # Inlet channel radius (mm)
        self.max_depth = max_depth  # Max branching generations
        self.channels = []  # Store generated acoustic voxel coordinates

    def thermal_density_multiplier(self, x, y):
        """
        Calculates branch density based on proximity to the 1000W logic core.
        Center of die (25, 25) requires maximum turbulence (highest density).

        Ironwood Thermal Map (single chip — 4.6 PFLOPS, 192 GB HBM3E):
          - Center (r < 10mm): 1000W logic core hotspot -> 1.5x density
          - Middle (10mm < r < 20mm): HBM3E memory stacks -> 1.0x density
          - Periphery (r > 20mm): Package edge -> 0.5x density

        Args:
            x, y: Position on the die surface (mm)

        Returns:
            Density multiplier (float) for branching depth at this position
        """
        center_x, center_y = self.die_size[0] / 2, self.die_size[1] / 2
        distance_to_core = np.sqrt((x - center_x)**2 + (y - center_y)**2)

        if distance_to_core < 10:
            return 1.5   # 1000W Core hotspot — maximum turbulent micro-channels
        elif distance_to_core < 20:
            return 1.0   # HBM3E Memory zone — standard branching
        else:
            return 0.5   # Periphery — wider, smoother channels (minimize delta-P)

    def generalized_murrays_law(self, parent_area, parent_length):
        """
        Applies Generalized Murray's Law scaling for non-circular
        (acoustic-friendly) cross sections.

        Standard Murray's Law: r_d = r_p * 2^(-1/3) ~ 0.794 * r_p
        Generalized (arbitrary cross-section):
            A_(i+1) = A_i * 2^(-2/3)
            L_(i+1) = L_i * 2^(-1/3)

        Args:
            parent_area: Cross-sectional area of parent channel (mm^2)
            parent_length: Length of parent channel segment (mm)

        Returns:
            (daughter_area, daughter_length) tuple in mm^2 and mm
        """
        daughter_area = parent_area * (2 ** (-2/3))
        daughter_length = parent_length * (2 ** (-1/3))
        return daughter_area, daughter_length

    def calculate_bifurcation_angles(self, parent_vector):
        """
        Calculates optimal branching vectors to minimize pressure drop.

        For symmetric bifurcation obeying Murray's Law, the optimal
        deviation angle from the parent direction is ~37.47 degrees.
        This minimizes total pumping power (hydrodynamic resistance)
        across the fractal network.

        Uses 2D rotation matrices to compute exact daughter branch
        direction vectors from the parent flow direction.

        Args:
            parent_vector: numpy array [vx, vy] — parent flow direction

        Returns:
            (vector_d1, vector_d2) — normalized direction vectors for
            left (+37.47 deg) and right (-37.47 deg) daughter branches
        """
        optimal_angle_rad = np.radians(37.47)

        # 2D rotation matrices for +theta and -theta
        rot_positive = np.array([
            [np.cos(optimal_angle_rad), -np.sin(optimal_angle_rad)],
            [np.sin(optimal_angle_rad),  np.cos(optimal_angle_rad)]
        ])
        rot_negative = np.array([
            [np.cos(-optimal_angle_rad), -np.sin(-optimal_angle_rad)],
            [np.sin(-optimal_angle_rad),  np.cos(-optimal_angle_rad)]
        ])

        # Apply rotations to the parent direction vector
        vector_d1 = np.dot(rot_positive, parent_vector)
        vector_d2 = np.dot(rot_negative, parent_vector)

        # Normalize vectors to ensure precise translation lengths
        vector_d1 = vector_d1 / np.linalg.norm(vector_d1)
        vector_d2 = vector_d2 / np.linalg.norm(vector_d2)

        return vector_d1, vector_d2

    def get_cross_section_shape(self, channel_area):
        """
        Calculates acoustic-friendly shape parameters for the ACU.

        Forces a rounded square cross-section to maximize thermal contact
        with the flat Ironwood die surface while eliminating 90-degree
        fluid stagnation dead zones that would occur with sharp corners.

        The height is set to 0.8x the width (flattened profile) to
        maximize the contact area with the die. Corner radius is 0.25x
        the width to eliminate acoustic shadows in the standing wave.

        Args:
            channel_area: Cross-sectional area of the channel (mm^2)

        Returns:
            dict with profile_type, width, height, corner_radius (all in mm)
        """
        # Area = width * (0.8 * width) -> width = sqrt(Area / 0.8)
        channel_width = np.sqrt(channel_area / 0.8)

        return {
            "profile_type": "rounded_square",
            "width": round(float(channel_width), 4),
            "height": round(float(channel_width * 0.8), 4),  # Flattened for die contact
            "corner_radius": round(float(channel_width * 0.25), 4)  # No acoustic shadows
        }

    def generate_constructal_network(self, start_pos, current_vector,
                                      current_depth, current_area,
                                      current_length):
        """
        Recursively generates the Variable-Density Constructal Network
        using exact vector translations and Murray bifurcation angles.

        At each bifurcation point:
          1. Check thermal map for local density requirement
          2. Apply Generalized Murray's Law to compute daughter dimensions
          3. Calculate rounded-square cross-section geometry
          4. Compute bifurcation vectors at +/-37.47 degrees
          5. Translate to exact branch endpoint coordinates
          6. Append ACU voxel data
          7. Recurse into left and right daughter branches

        Args:
            start_pos: numpy array [x, y] — position on die surface (mm)
            current_vector: numpy array [vx, vy] — parent flow direction
            current_depth: Current branching generation (0 = inlet)
            current_area: Cross-sectional area of current channel (mm^2)
            current_length: Length of current channel segment (mm)
        """
        # Base case: max depth reached or channel too small for acoustic resolution
        # Minimum 0.5mm^2 channel area — PENDING DeepSeek acoustic validation
        if current_depth >= self.max_depth or current_area < 0.5:
            return

        x, y = start_pos

        # Apply thermal density mask from Ironwood heat map
        density_mod = self.thermal_density_multiplier(x, y)
        adjusted_max_depth = self.max_depth * density_mod

        if current_depth >= adjusted_max_depth:
            return

        # Calculate daughter dimensions via Generalized Murray's Law
        d_area, d_length = self.generalized_murrays_law(current_area,
                                                         current_length)

        # Calculate rounded-square cross-section for ACU
        d_geometry = self.get_cross_section_shape(d_area)

        # Calculate exact bifurcation vectors (+/-37.47 degrees)
        vector_left, vector_right = self.calculate_bifurcation_angles(
            current_vector)

        # Translate coordinates to find exact branching endpoints
        branch_left_pos = start_pos + (vector_left * d_length)
        branch_right_pos = start_pos + (vector_right * d_length)

        # Append data to the ACU compilation list
        self.channels.append({
            "start": tuple(np.round(start_pos, 3)),
            "end_left": tuple(np.round(branch_left_pos, 3)),
            "end_right": tuple(np.round(branch_right_pos, 3)),
            "area": round(float(d_area), 3),
            "length": round(float(d_length), 3),
            "geometry": d_geometry,
            "depth": current_depth + 1
        })

        # Recurse into left and right daughter branches
        self.generate_constructal_network(
            branch_left_pos, vector_left,
            current_depth + 1, d_area, d_length)
        self.generate_constructal_network(
            branch_right_pos, vector_right,
            current_depth + 1, d_area, d_length)


# =============================================================================
# Memphis Node Zero — Ironwood TPU Thermal Simulator Configuration
# =============================================================================

if __name__ == "__main__":
    # Initialize generator for Memphis Node Zero test case
    ironwood_manifold = HTAM_Fractal_Generator(
        die_size=(50, 50),   # mm — single Ironwood chip footprint
        base_radius=2.5,     # mm — inlet channel radius
        max_depth=6           # branching generations
    )

    # Initial cross-sectional area (rectangular approximation of base channel)
    # Width = 2 * base_radius = 5mm, Height = 2mm (acoustic basin constraint)
    initial_area = 10.0       # mm^2  (5mm x 2mm)
    initial_length = 10.0     # mm — first segment length

    # Inlet starts at center-top (25, 0) and flows downward along the Y-axis
    inlet_pos = np.array([25.0, 0.0])
    inlet_vector = np.array([0.0, 1.0])

    # Generate the fractal network
    # Output: ACU voxel coordinates for acoustic standing wave programming
    ironwood_manifold.generate_constructal_network(
        start_pos=inlet_pos,
        current_vector=inlet_vector,
        current_depth=0,
        current_area=initial_area,
        current_length=initial_length
    )

    # --- Output Summary ---
    print(f"--- Memphis Node Zero HTAM Voxel Map v1.1 ---")
    print(f"Die size: {ironwood_manifold.die_size[0]}mm x "
          f"{ironwood_manifold.die_size[1]}mm")
    print(f"Total fractal segments compiled: "
          f"{len(ironwood_manifold.channels)}")
    print(f"Symmetric Bifurcation Angle: +/-37.47 deg")
    print(f"Cross-Section Geometry: Rounded Square (variable scaling)")
    print(f"Status: READY FOR ACU PHASE MAP GENERATION")
    print()

    # Print first few channel segments for verification
    if ironwood_manifold.channels:
        print(f"--- Sample Channel Data (first 3 segments) ---")
        for i, ch in enumerate(ironwood_manifold.channels[:3]):
            print(f"  Segment {i+1} (depth {ch['depth']}):")
            print(f"    Start: {ch['start']}")
            print(f"    Left branch endpoint:  {ch['end_left']}")
            print(f"    Right branch endpoint: {ch['end_right']}")
            print(f"    Area: {ch['area']} mm^2")
            print(f"    Length: {ch['length']} mm")
            print(f"    Width: {ch['geometry']['width']} mm")
            print(f"    Height: {ch['geometry']['height']} mm")
            print(f"    Corner radius: {ch['geometry']['corner_radius']} mm")
            print()

    print(f"Next: DeepSeek plugs channel data into ACU acoustic simulator")
    print(f"Question: Will 0.5mm minimum channel width hold shape "
          f"in standing wave?")