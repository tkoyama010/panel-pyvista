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
    nframe = 150
    step = param.Integer(default=1, bounds=(0, nframe))

    value = np.linspace(0, 10 * np.pi, nframe + 1)

    @param.depends("step")
    def view(self):
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

pn.extension()
pn.Column(
    pn.Param(viewer.param, widgets={"step": pn.widgets.Player}),
    pn.panel(viewer.view, width=1000),
).show()
