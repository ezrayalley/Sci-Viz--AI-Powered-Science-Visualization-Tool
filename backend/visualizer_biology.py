from manim import *
import numpy as np

class EnzymeKinetics(Scene):
    def construct(self):
        title = Text("Enzyme Kinetics - Michaelis-Menten Curve", font_size=32).to_edge(UP)
        self.play(Write(title))

        # Axes setup
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            x_length=8,
            y_length=4.5,
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="[S] (Substrate Concentration)", y_label="v (Rate)")
        axes_group = VGroup(axes, labels).shift(DOWN * 0.5)

        self.play(Create(axes), Write(labels))

        # Constants
        Vmax = 1.0
        Km = 2.0

        def michaelis_menten(S):
            return (Vmax * S) / (Km + S)

        # Draw the curve
        curve = axes.plot(lambda x: michaelis_menten(x), color=BLUE, x_range=[0.1, 10], use_smoothing=True)
        self.play(Create(curve))
        self.wait(1)

        # Highlight Vmax and Km
        vmax_line = axes.get_horizontal_line(axes.c2p(0, Vmax), color=YELLOW)
        vmax_label = MathTex("V_{max}").next_to(vmax_line, RIGHT)

        km_dot = Dot(axes.c2p(Km, michaelis_menten(Km)), color=RED)
        km_label = MathTex("K_m").next_to(km_dot, DOWN)

        self.play(Create(vmax_line), Write(vmax_label))
        self.play(FadeIn(km_dot), Write(km_label))
        self.wait(1)

        # Animate substrate increase
        tracker = ValueTracker(0.1)

        moving_dot = always_redraw(
            lambda: Dot(axes.c2p(tracker.get_value(), michaelis_menten(tracker.get_value())), color=GREEN)
        )
        sub_label = always_redraw(
            lambda: MathTex(f"[S] = {tracker.get_value():.1f}").next_to(moving_dot, UP)
        )

        self.play(FadeIn(moving_dot), FadeIn(sub_label))
        self.play(tracker.animate.set_value(9), run_time=6, rate_func=linear)
        self.wait(2)

class PopulationGrowth(Scene):
    def construct(self):
        title = Text("Population Growth: Exponential vs Logistic", font_size=32).to_edge(UP)
        self.play(Write(title))

        # Axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 12, 2],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="Time (t)", y_label="Population (P)")
        axes_group = VGroup(axes, labels).shift(DOWN * 0.5)

        self.play(Create(axes), Write(labels))

        # Constants
        P0 = 1
        r = 0.6
        K = 10  # Carrying capacity for logistic
        A = (K - P0) / P0

        # Define growth functions
        def exponential(t):
            return P0 * np.exp(r * t)

        def logistic(t):
            return K / (1 + A * np.exp(-r * t))

        # Graphs
        exp_curve = axes.plot(lambda t: exponential(t), x_range=[0, 5], color=BLUE, stroke_width=4)
        log_curve = axes.plot(lambda t: logistic(t), x_range=[0, 10], color=GREEN, stroke_width=4)

        exp_label = MathTex("P(t) = P_0 e^{rt}", color=BLUE).scale(0.6).next_to(exp_curve, UP).shift(LEFT*2)
        log_label = MathTex("P(t) = \dfrac{K}{1 + Ae^{-rt}}", color=GREEN).scale(0.6).next_to(log_curve, DOWN).shift(RIGHT)

        self.play(Create(exp_curve), Write(exp_label))
        self.wait(1)
        self.play(Create(log_curve), Write(log_label))

        # Carrying capacity line
        k_line = axes.get_horizontal_line(axes.c2p(0, K), color=YELLOW, stroke_width=3)
        k_label = MathTex("K", color=YELLOW).next_to(k_line, RIGHT)
        self.play(Create(k_line), Write(k_label))
        self.wait(1)

        # Animate r increase effect
        tracker = ValueTracker(0.6)

        updated_log = always_redraw(
            lambda: axes.plot(lambda t: K / (1 + A * np.exp(-tracker.get_value() * t)), x_range=[0, 10], color=RED)
        )

        self.play(FadeOut(log_curve), FadeIn(updated_log))
        self.play(tracker.animate.set_value(1.2), run_time=4)
        self.wait(2)

class CellDivisionMitosis(Scene):
    def construct(self):
        title = Text("Cell Division - Mitosis", font_size=36).to_edge(UP)
        self.play(Write(title))

        phases = ["Prophase", "Metaphase", "Anaphase", "Telophase"]
        colors = [BLUE, GREEN, RED, ORANGE]
        
        for i, phase in enumerate(phases):
            self.play(self.get_phase_animation(phase, colors[i]))
            self.wait(1.5)

        done = Text("Mitosis Complete: 2 Identical Daughter Cells", font_size=28, color=YELLOW).shift(DOWN*2)
        self.play(Write(done))
        self.wait(2)

    def get_phase_animation(self, phase, color):
        label = Text(phase, font_size=28, color=color).to_edge(DOWN)

        # Circle as cell
        cell = Circle(radius=2, color=WHITE).shift(UP * 0.5)

        # Nucleus (initial)
        nucleus = Circle(radius=0.8, color=color, fill_opacity=0.5).move_to(cell.get_center())

        animations = {
            "Prophase": [Create(cell), FadeIn(nucleus), Write(label)],

            "Metaphase": [
                FadeOut(nucleus),
                self.draw_chromosomes(position="center"),
                Write(label)
            ],

            "Anaphase": [
                self.draw_chromosomes(position="split"),
                Write(label)
            ],

            "Telophase": [
                self.show_two_cells(),
                Write(label)
            ]
        }

        return AnimationGroup(*animations[phase], lag_ratio=0.3)

    def draw_chromosomes(self, position="center"):
        chromo_color = PURPLE
        lines = []
        if position == "center":
            for x in [-0.5, 0, 0.5]:
                lines.append(Line([x, 0, 0], [x, 1, 0], color=chromo_color))
        elif position == "split":
            for x in [-1.5, -1, 1, 1.5]:
                lines.append(Line([x, 0, 0], [x, 1, 0], color=chromo_color))
        return AnimationGroup(*[Create(line) for line in lines])

    def show_two_cells(self):
        cell1 = Circle(radius=1.2, color=WHITE).shift(LEFT * 2 + DOWN * 0.5)
        cell2 = Circle(radius=1.2, color=WHITE).shift(RIGHT * 2 + DOWN * 0.5)
        n1 = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).move_to(cell1.get_center())
        n2 = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).move_to(cell2.get_center())
        return AnimationGroup(Create(cell1), Create(cell2), FadeIn(n1), FadeIn(n2))
