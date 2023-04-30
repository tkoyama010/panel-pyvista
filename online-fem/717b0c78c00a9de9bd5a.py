import holoviews as hv
import panel as pn
import pyvista as pv

pv.set_plot_theme("document")

hv.extension("bokeh")
pn.extension()
pn.extension("vtk", sizing_mode="stretch_width")

filename_input = pn.widgets.TextInput(
    name="CSVファイルパス入力", placeholder="ここにCSVファイルのパスを入力してください"
)

filename_input.placeholder = "HogeHoge FugaFuga"
filename_input.servable()

load_file_button = pn.widgets.Button(name="ファイル読み込み", button_type="primary")
load_file_button.servable()

x_axis_select = pn.widgets.Select(name="X軸")
y_axis_select = pn.widgets.Select(name="Y軸")
display_graph_button = pn.widgets.Button(
    name="グラフ描画", button_type="primary", disabled=True
)
display_graph_button.servable()

blank_hv = hv.Scatter((1, 1))
graph_pane = pn.pane.HoloViews(blank_hv, visible=False)
pn.pane.HoloViews(blank_hv, visible=True).servable()

plotter = pv.Plotter()
cyl = pv.Cylinder()
plotter.add_mesh(cyl)
pn.panel(plotter.ren_win).servable()
