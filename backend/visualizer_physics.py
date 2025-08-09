from manim import *
import numpy as np

# 🚀 Projectile Motion
from manim import *

import numpy as np

class ProjectileMotion(Scene):
    def construct(self):
        # Title
        title = Text("Projectile Motion", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Axes (raise Y-axis visually by shifting everything up)
        axes = Axes(
            x_range=[0, 15, 1],  # Extend X for wider motion
            y_range=[0, 12, 1],  # Taller Y
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 0.5 + UP * 1)  # Lift the whole plot upward

        labels = axes.get_axis_labels("x", "y")

        eq1 = MathTex("x = v_0 \\cos(\\theta)t").scale(0.7).next_to(axes, RIGHT).shift(LEFT * 2)
        eq2 = MathTex("y = v_0 \\sin(\\theta)t - \\frac{1}{2}gt^2").scale(0.7).next_to(eq1, DOWN)

        self.play(Create(axes), Write(labels))
        self.wait(1)
        self.play(Write(eq1), Write(eq2))

        # Increased velocity and same angle
        v0 = 10          # 🔼 Increased from 6 to 10
        theta = PI / 4
        g = 9.8

        # Compute trajectory path points
        t_max = (2 * v0 * np.sin(theta)) / g
        t_vals = np.linspace(0, t_max, 60)

        points = [
            axes.c2p(v0 * np.cos(theta) * t, v0 * np.sin(theta) * t - 0.5 * g * t**2)
            for t in t_vals
        ]

        path = VMobject(color=BLUE)
        path.set_points_smoothly(points)

        dot = Dot(color=RED).move_to(path.points[0])
        self.play(Create(path))
        self.play(GrowFromCenter(dot))
        self.play(MoveAlongPath(dot, path), run_time=4, rate_func=linear)
        self.wait()
# 🔁 Simple Harmonic Motion (SHM)
from manim import *

class SHMCombinedScene(Scene):
    def construct(self):
        # === Title ===
        title = Text("Simple Harmonic Motion", font_size=36).to_edge(UP)
        self.play(Write(title))

        # === LEFT SIDE: SINE WAVE ===
        wave_axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": False}
        ).to_edge(LEFT).shift(DOWN * 0.5)

        sine_wave = wave_axes.plot(lambda x: np.sin(x), color=BLUE)

        wave_label = Text("Wave", color=BLUE, font_size=24).next_to(wave_axes, UP).shift(LEFT)
        amp_arrow = DoubleArrow(
            wave_axes.c2p(1.5, 0), wave_axes.c2p(1.5, 1),
            buff=0.1, color=YELLOW
        )
        amp_label = Text("Amplitude", font_size=20).next_to(amp_arrow, RIGHT, buff=0.1)

        eq_arrow = DoubleArrow(
            wave_axes.c2p(2*np.pi, 0), wave_axes.c2p(4*np.pi, 0),
            buff=0.1, color=GREEN
        )
        eq_label = Text("Equal Interval", font_size=20).next_to(eq_arrow, DOWN, buff=0.1)

        self.play(Create(wave_axes), Create(sine_wave))
        self.play(Write(wave_label))
        self.play(Create(amp_arrow), Write(amp_label))
        self.play(Create(eq_arrow), Write(eq_label))

        # === RIGHT SIDE: PENDULUM ===
        pivot = RIGHT * 3 + UP * 1.5
        pend_length = 2
        swing_angle = PI / 6  # 30 degrees

        rod = Line(pivot, pivot + pend_length * DOWN).rotate(swing_angle, about_point=pivot)
        bob = Dot(rod.get_end(), radius=0.2, color=ORANGE)
        pendulum = VGroup(rod, bob)

        # Static elements
        mean_line = DashedLine(pivot, pivot + DOWN * pend_length, color=GRAY)
        mean_label = Text("Mean\nPosition", font_size=20).next_to(mean_line, DOWN)

        extreme_right = Dot(pivot + pend_length * DOWN).rotate_about_origin(swing_angle)
        left_label = Text("Extreme\nPosition", font_size=18).next_to(rod.get_end(), LEFT + DOWN, buff=0.2)
        right_label = Text("Extreme\nPosition", font_size=18).next_to(extreme_right, RIGHT + DOWN, buff=0.2)

        bob_label = Text("Bob", font_size=20, color=BLACK).move_to(bob.get_center())
        weight_arrow = Arrow(bob.get_center(), bob.get_center() + DOWN * 0.7, buff=0.05, color=RED)
        weight_label = MathTex("W = mg", color=RED).scale(0.7).next_to(weight_arrow, DOWN)

        # Show pendulum
        self.play(Create(mean_line), Write(mean_label))
        self.play(Create(rod), GrowFromCenter(bob), Write(bob_label))
        self.play(Create(weight_arrow), Write(weight_label))
        self.play(Write(left_label), Write(right_label))

        # Animate swinging
        for _ in range(2):
            self.play(pendulum.animate.rotate(-swing_angle * 2, about_point=pivot), run_time=1, rate_func=smooth)
            self.play(pendulum.animate.rotate(swing_angle * 2, about_point=pivot), run_time=1, rate_func=smooth)

        self.wait()



# 🌀 Circular Motion
class CircularMotion(Scene):
    def construct(self):
        title = Text("Uniform Circular Motion", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Axes for reference
        x_axis = NumberLine(x_range=[-3, 3], length=6).shift(DOWN * 2)
        y_axis = NumberLine(x_range=[-3, 3], length=6).rotate(PI / 2).shift(LEFT * 2)

        self.play(Create(x_axis), Create(y_axis))

        # Circle and motion
        circle = Circle(radius=2, color=BLUE)
        center = Dot(circle.get_center(), color=WHITE)
        dot = Dot(color=GREEN).move_to(circle.point_at_angle(0))
        radius_line = always_redraw(lambda: Line(circle.get_center(), dot.get_center(), color=GRAY))

        velocity_label = always_redraw(
            lambda: MathTex("v").scale(0.7).next_to(dot, RIGHT)
        )

        self.play(Create(circle), GrowFromCenter(center), GrowFromCenter(dot))
        self.add(radius_line, velocity_label)

        self.play(Rotating(dot, about_point=circle.get_center(), angle=2 * PI, run_time=4))
        self.wait()

