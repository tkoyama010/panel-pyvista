import panel as pn
import param
import pyvista as pv
from IPython.display import IFrame

pn.extension(template="fast")

def handler(viewer, src, **kwargs):
    return IFrame(src, width="1450", height="750")


class PyVistaViewer(param.Parameterized):
    mesh_name = param.ObjectSelector(
        default="cylinder",
        objects=[
            "cylinder",
            "arrow",
            "sphere",
            "plane",
            "line",
            "box",
            "cone",
            "poly",
            "disc",
        ],
    )
    line_width = param.Number(default=1, bounds=(0, 10))
    plotter = pv.Plotter(notebook=True)
    mesh = {
        "cylinder": pv.Cylinder(),
        "arrow": pv.Arrow(),
        "sphere": pv.Sphere(),
        "plane": pv.Plane(),
        "line": pv.Line(),
        "box": pv.Box(),
        "cone": pv.Cone(),
        "poly": pv.Polygon(),
        "disc": pv.Disc(),
    }

    @param.depends("mesh_name", "line_width")
    def view(self):
        self.plotter.clear()
        self.plotter.add_mesh(
            self.mesh[self.mesh_name],
            color="tan",
            show_edges=True,
            line_width=self.line_width,
        )
        iframe = self.plotter.show(
            jupyter_backend="trame",
            jupyter_kwargs=dict(handler=handler),
            return_viewer=True,
        )
        return iframe


viewer = PyVistaViewer(name="PyVista Viewer")

pn.Column(viewer.param).servable(target="sidebar")
pn.Column(viewer.view).servable(target="main")
