import panel as pn
import param
import pyvista as pv
from IPython.display import IFrame


def handler(viewer, src, **kwargs):
    return IFrame(src, "100%", "1000px")


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

    @param.depends("mesh_name")
    def view(self):
        self.plotter.clear()
        self.plotter.add_mesh(self.mesh[self.mesh_name], color="tan", show_edges=True)
        iframe = self.plotter.show(
            jupyter_backend="trame",
            jupyter_kwargs=dict(handler=handler),
            return_viewer=True,
        )
        return iframe


viewer = PyVistaViewer(name="PyVista Viewer")

pn.extension()
pn.Row(viewer.param, pn.panel(viewer.view, width=1000)).show()
