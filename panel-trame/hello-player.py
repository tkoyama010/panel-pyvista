import numpy as np
import panel as pn
import param
import pyvista as pv
from IPython.display import IFrame


def handler(viewer, src, **kwargs):
    return IFrame(src, "100%", "1000px")


class PyVistaViewer(param.Parameterized):
    x = np.arange(-10, 10, 0.5)
    y = np.arange(-10, 10, 0.5)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x**2 + y**2)
    z = np.sin(r)

    # Create and structured surface
    grid = pv.StructuredGrid(x, y, z)

    # Create a plotter object and set the scalars to the Z height
    plotter = pv.Plotter(notebook=True, off_screen=False)
    plotter.add_mesh(
        grid,
        scalars=z.ravel(),
        lighting=False,
        show_edges=True,
        scalar_bar_args={"title": "Height"},
        clim=[-1, 1],
    )
    plotter.add_text("0 step", name="title", position="upper_right", render=False)
    nframe = 150
    step = param.Integer(default=1, bounds=(0, nframe))
    value = np.linspace(0, 10 * np.pi, nframe + 1)

    @param.depends("step")
    def view(self):
        self.plotter.remove_actor("title", render=False)
        self.plotter.add_text(
            str(self.step) + "step", name="title", render=False, position="upper_right"
        )
        pts = self.grid.points.copy()

        # Update Z and write a frame for each updated position
        z = np.sin(self.r + self.value[self.step])
        pts[:, -1] = z.ravel()
        self.plotter.update_coordinates(pts, render=False)
        self.plotter.update_scalars(z.ravel(), render=False)

        # Write a frame. This triggers a render.
        # self.plotter.update()

        # Open a gif
        iframe = self.plotter.show(
            jupyter_backend="trame",
            jupyter_kwargs=dict(handler=handler),
            return_viewer=True,
            interactive_update=True,
        )
        return iframe


viewer = PyVistaViewer(name="PyVista Viewer")

player = pn.widgets.Player(name="Player", start=0, end=150, value=0, loop_policy="once")

pn.extension()

pn.Column(
    pn.Row(
        player.controls(jslink=True),
        pn.panel(viewer.view, width=1000),
    ),
    pn.Param(viewer.param, widgets={"step": player}),
).show()
