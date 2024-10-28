import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1('Ejemplo Básico de Dash'),
    
    html.Div([
        dcc.Input(id='input-text', value='Escribe algo', type='text'),
        html.Div(id='output-text')
    ]),
    
    html.Div([
        dcc.Graph(id='scatter-plot')
    ])
])

# Callback para actualizar el texto de salida
@app.callback(
    Output('output-text', 'children'),
    Input('input-text', 'value')
)
def update_output(value):
    return f'Has escrito: {value}'

# Datos para el gráfico
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# Callback para mostrar el gráfico
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('input-text', 'value')  # Puede ser utilizado para cambiar el gráfico basado en el input
)
def update_graph(value):
    return fig

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
