import panel as pn
import pyvista as pv

pv.set_plot_theme("document")

cyl = pv.Cylinder()
arrow = pv.Arrow()
sphere = pv.Sphere()
plane = pv.Plane()
line = pv.Line()
box = pv.Box()
cone = pv.Cone()
poly = pv.Polygon()
disc = pv.Disc()


plotter = pv.Plotter(shape=(3, 3))
# Top row
plotter.subplot(0, 0)
plotter.add_mesh(cyl, color="tan", show_edges=True)
plotter.subplot(0, 1)
plotter.add_mesh(arrow, color="tan", show_edges=True)
plotter.subplot(0, 2)
plotter.add_mesh(sphere, color="tan", show_edges=True)
# Middle row
plotter.subplot(1, 0)
plotter.add_mesh(plane, color="tan", show_edges=True)
plotter.subplot(1, 1)
plotter.add_mesh(line, color="tan", line_width=3)
plotter.subplot(1, 2)
plotter.add_mesh(box, color="tan", show_edges=True)
# Bottom row
plotter.subplot(2, 0)
plotter.add_mesh(cone, color="tan", show_edges=True)
plotter.subplot(2, 1)
plotter.add_mesh(poly, color="tan", show_edges=True)
plotter.subplot(2, 2)
plotter.add_mesh(disc, color="tan", show_edges=True)

plot = plotter.ren_win
pn.panel(plot, height=700, sizing_mode="stretch_both").servable()
