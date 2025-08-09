from manim import *
import numpy as np

class ArrheniusEquation(Scene):
    def construct(self):
        title = Text("Arrhenius Equation", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Equation
        eq = MathTex("k = A e^{-E_a / RT}").scale(1.2).next_to(title, DOWN)
        self.play(Write(eq))
        self.wait(1)

        # Axes setup
        axes = Axes(
            x_range=[250, 500, 50],
            y_range=[0, 1000, 200],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True},
            tips=True
        )
        labels = axes.get_axis_labels(x_label="T (K)", y_label="k")
        graph_group = VGroup(axes, labels).scale(0.9).shift(DOWN)
        self.play(Create(axes), Write(labels))

        # Constants
        A = 10000
        Ea = 50000  # J/mol
        R = 8.314

        # k = A * exp(-Ea / (R * T))
        def rate_constant(T):
            return A * np.exp(-Ea / (R * T))

        graph = axes.plot(lambda t: rate_constant(t), color=BLUE, x_range=[250, 500])
        self.play(Create(graph))

        # Label important points
        t_val = 300
        k_val = rate_constant(t_val)
        dot = Dot(axes.c2p(t_val, k_val), color=YELLOW)
        label = MathTex("T = 300K").next_to(dot, UP)
        self.play(FadeIn(dot), Write(label))
        self.wait()

        # Animate temperature increase
        tracker = ValueTracker(300)

        moving_dot = always_redraw(
            lambda: Dot(axes.c2p(tracker.get_value(), rate_constant(tracker.get_value())), color=RED)
        )

        temp_label = always_redraw(
            lambda: MathTex(f"T = {int(tracker.get_value())}K").next_to(moving_dot, UP)
        )

        self.play(FadeOut(dot), FadeOut(label))
        self.play(FadeIn(moving_dot), FadeIn(temp_label))
        self.play(tracker.animate.set_value(450), run_time=5, rate_func=linear)

        self.wait(2)

class BoyleLaw(Scene):
    def construct(self):
        title = Text("Boyle's Law: PV = constant", font_size=36).to_edge(UP)
        self.play(Write(title))

        eq = MathTex("P V = k").scale(1.2).next_to(title, DOWN)
        self.play(Write(eq))
        self.wait(1)

        # Axes setup
        axes = Axes(
            x_range=[1, 10, 1],
            y_range=[0, 10, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True},
            tips=True
        )
        labels = axes.get_axis_labels(x_label="Volume (V)", y_label="Pressure (P)")
        self.play(Create(axes), Write(labels))

        k = 10  # P * V = k
        graph = axes.plot(lambda v: k / v, color=GREEN, x_range=[1, 10])
        self.play(Create(graph))

        tracker = ValueTracker(2)

        dot = always_redraw(
            lambda: Dot(axes.c2p(tracker.get_value(), k / tracker.get_value()), color=RED)
        )

        label = always_redraw(
            lambda: MathTex(f"V = {tracker.get_value():.1f}L").next_to(dot, UP)
        )

        self.play(FadeIn(dot), FadeIn(label))
        self.play(tracker.animate.set_value(9), run_time=5, rate_func=linear)
        self.wait(2)

class CharlesLaw(Scene):
    def construct(self):
        title = Text("Charles's Law: V/T = constant", font_size=36).to_edge(UP)
        self.play(Write(title))

        eq = MathTex("V \propto T").scale(1.2).next_to(title, DOWN)
        self.play(Write(eq))
        self.wait(1)

        # Axes
        axes = Axes(
            x_range=[0, 400, 50],
            y_range=[0, 10, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True},
            tips=True
        )
        labels = axes.get_axis_labels(x_label="Temperature (K)", y_label="Volume (L)")
        self.play(Create(axes), Write(labels))

        slope = 0.02  # V = slope * T
        graph = axes.plot(lambda T: slope * T, color=ORANGE, x_range=[0, 400])
        self.play(Create(graph))

        tracker = ValueTracker(100)

        dot = always_redraw(
            lambda: Dot(axes.c2p(tracker.get_value(), slope * tracker.get_value()), color=BLUE)
        )

        label = always_redraw(
            lambda: MathTex(f"T = {int(tracker.get_value())}K").next_to(dot, UP)
        )

        self.play(FadeIn(dot), FadeIn(label))
        self.play(tracker.animate.set_value(350), run_time=5, rate_func=linear)
        self.wait(2)

class EnergyProfile(Scene):
    def construct(self):
        title = Text("Energy Profile of a Chemical Reaction", font_size=34).to_edge(UP)
        self.play(Write(title))

        eq = MathTex("\Delta H = E_{products} - E_{reactants}").scale(1).next_to(title, DOWN)
        self.play(Write(eq))
        self.wait(1)

        # Axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 8, 1],
            x_length=9,
            y_length=5,
            axis_config={"include_numbers": False},
            tips=False
        )
        labels = axes.get_axis_labels(x_label="Reaction Pathway", y_label="Energy")
        self.play(Create(axes), Write(labels))

        def energy_profile(x):
            return 5 * np.exp(-((x - 5) ** 2) / 1.5) + 1.5  # Gaussian bump + offset

        curve = axes.plot(energy_profile, color=PURPLE)
        self.play(Create(curve))

        # Labels for reactants, transition state, products
        reactant_dot = Dot(axes.c2p(0.5, energy_profile(0.5)), color=GREEN)
        ts_dot = Dot(axes.c2p(5, energy_profile(5)), color=YELLOW)
        product_dot = Dot(axes.c2p(9, energy_profile(9)), color=RED)

        reactant_label = Text("Reactants", font_size=24).next_to(reactant_dot, LEFT)
        ts_label = Text("Transition State", font_size=24).next_to(ts_dot, UP)
        product_label = Text("Products", font_size=24).next_to(product_dot, RIGHT)

        self.play(FadeIn(reactant_dot), Write(reactant_label))
        self.play(FadeIn(ts_dot), Write(ts_label))
        self.play(FadeIn(product_dot), Write(product_label))

        self.wait(2)
