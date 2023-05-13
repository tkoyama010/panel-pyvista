import panel as pn
import param
import pyvista as pv
from IPython.display import IFrame

plotter = pv.Plotter(notebook=True)

cyl = pv.Cylinder()
arrow = pv.Arrow()
sphere = pv.Sphere()
plane = pv.Plane()
line = pv.Line()
box = pv.Box()
cone = pv.Cone()
poly = pv.Polygon()
disc = pv.Disc()


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

    @param.depends("mesh_name")
    def view(self):
        plotter.clear()
        if self.mesh_name == "cylinder":
            plotter.add_mesh(cyl, color="tan", show_edges=True)
        if self.mesh_name == "arrow":
            plotter.add_mesh(arrow, color="tan", show_edges=True)
        if self.mesh_name == "sphere":
            plotter.add_mesh(sphere, color="tan", show_edges=True)
        if self.mesh_name == "plane":
            plotter.add_mesh(plane, color="tan", show_edges=True)
        if self.mesh_name == "line":
            plotter.add_mesh(line, color="tan", line_width=3)
        if self.mesh_name == "box":
            plotter.add_mesh(box, color="tan", show_edges=True)
        if self.mesh_name == "cone":
            plotter.add_mesh(cone, color="tan", show_edges=True)
        if self.mesh_name == "poly":
            plotter.add_mesh(poly, color="tan", show_edges=True)
        if self.mesh_name == "disc":
            plotter.add_mesh(disc, color="tan", show_edges=True)
        iframe = plotter.show(
            jupyter_backend="trame",
            jupyter_kwargs=dict(handler=handler),
            return_viewer=True,
        )
        return iframe


viewer = PyVistaViewer(name="PyVista Viewer")

pn.extension()
pn.Row(viewer.param, pn.panel(viewer.view, width=1000)).show()
