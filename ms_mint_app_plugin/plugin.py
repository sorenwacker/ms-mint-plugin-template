from ms_mint_app.plugin_interface import PluginInterface
from dash import html, dcc



class TemplatePlugin(PluginInterface):
    def __init__(self):
        self._label = _label
        self._order = 100

    def layout(self):
        return _layout

    def callbacks(self, app, fsc, cache):
        callbacks(app, fsc, cache)
    
    def outputs(self):
        return _outputs

    
_label = 'Plugin'    
    
    
_layout = html.Div([html.H1('Plugin')])    
    
    
_outputs = html.Div(
    id="template-outputs",
    children=[
        html.Div(id={"index": "template-output", "type": "output"}),
    ],
)

def  callbacks(app, fsc, cache):
    pass
