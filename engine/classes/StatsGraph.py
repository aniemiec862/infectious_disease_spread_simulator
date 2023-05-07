import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab
import pygame

class StatsGraph:
    def __init__(self, renderer, x_offset, y_offset, downsample_factor=100):
        self.renderer = renderer
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.susceptible = []
        self.infected = []
        self.recovered = []
        self.downsample_factor = downsample_factor

        matplotlib.use("Agg")

    def update(self, susceptible, infected, recovered):
        self.susceptible.append(susceptible)
        self.infected.append(infected)
        self.recovered.append(recovered)

        if len(self.susceptible) > self.downsample_factor:
            self.susceptible = self.susceptible[-self.downsample_factor:]
            self.infected = self.infected[-self.downsample_factor:]
            self.recovered = self.recovered[-self.downsample_factor:]

        fig = pylab.figure(figsize=[4, 4],  # Inches
                           dpi=100,  # 100 dots per inch, so the resulting buffer is 400x400 pixels
                           )
        ax = fig.gca()
        ax.plot(self.susceptible, label='S(t)')
        ax.plot(self.infected, label='I(t)')
        ax.plot(self.recovered, label='R(t)')
        ax.legend()
        ax.set_xticklabels(labels=[])

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()

        size = canvas.get_width_height()
        graph = pygame.image.fromstring(raw_data, size, "RGB")

        self.renderer.render_graph(graph, self.x_offset, self.y_offset)
        pylab.close(fig)
