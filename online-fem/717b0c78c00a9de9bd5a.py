import panel as pn

pn.extension()

filename_input = pn.widgets.TextInput(
    name="CSVファイルパス入力", placeholder="ここにCSVファイルのパスを入力してください"
)

filename_input.placeholder = "HogeHoge FugaFuga"
filename_input.servable()
