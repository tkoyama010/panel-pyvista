import panel as pn
import param
import pyvista as pv
from IPython.display import IFrame


class Viewer(param.Parameterized):
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
    plotter = pv.Viewer(notebook=True)
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

    def handler(self, viewer, src, **kwargs):
        return IFrame(src, "100%", "1000px")

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
            jupyter_kwargs=dict(handler=self.handler),
            return_viewer=True,
        )
        return iframe


viewer = Viewer(name="Viewer")

pn.extension()
pn.Row(viewer.param, pn.panel(viewer.view, width=1000)).show()
