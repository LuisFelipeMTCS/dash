import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px

# Inicialização do aplicativo Dash
app = dash.Dash(__name__)

# Dados para os gráficos
df = pd.DataFrame({
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [10, 20, 30, 40],
    'X': [1, 2, 3, 4],
    'Y': [10, 20, 30, 40],
    'Z': [5, 15, 25, 35]
})

cores_graficos = {
    'background': '#212121',
    'text': '#FFFFFF',
    'plot_bgcolor': '#303030',
    'paper_bgcolor': '#424242',
    'border_color': '#FFFFFF'
}

# Função para configurar layout de gráfico
def configurar_layout(fig, title):
    fig.update_layout(
        title=title,
        title_font=dict(size=20, color=cores_graficos['text'], family="Arial"),
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor=cores_graficos['paper_bgcolor'],
        plot_bgcolor=cores_graficos['plot_bgcolor'],
        font=dict(size=12, family="Arial", color=cores_graficos['text']),
        autosize=True,
        width=650,
        height=400,
        showlegend=False,
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        xaxis_zeroline=False,
        yaxis_zeroline=False
    )
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

# Criação dos gráficos
fig_line = px.line(df, x='X', y='Y', markers=True)
configurar_layout(fig_line, 'Gráfico de Linhas')

fig_bar = px.bar(df, x='Categoria', y='Valores', text='Valores')
configurar_layout(fig_bar, 'Gráfico de Barras')
fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')

fig_scatter = px.scatter(df, x='X', y='Y', size='Z', color='Categoria', hover_name='Categoria')
configurar_layout(fig_scatter, 'Gráfico de Dispersão')

fig_pie = px.pie(df, values='Valores', names='Categoria', hole=0.3)
configurar_layout(fig_pie, 'Gráfico de Pizza')

# Layout do aplicativo Dash
app.layout = html.Div(style={'backgroundColor': cores_graficos['background'], 'padding': '20px'}, children=[
    html.H1(children='Dashboard Protótipo Fiap', style={'textAlign': 'center', 'color': cores_graficos['text']}),

    html.Div( style={'textAlign': 'center', 'color': cores_graficos['text'], 'margin-bottom': '30px'}),

    html.Div(className='row', style={'display': 'flex', 'justifyContent': 'center'}, children=[
        html.Div(className='six columns', style={'margin-right': '10px', 'border-radius': '10px'}, children=[
            dcc.Graph(id='graph1', figure=fig_line, style={'width': '100%', 'height': '100%'})
        ]),
        html.Div(className='six columns', style={'margin-left': '10px', 'border-radius': '10px'}, children=[
            dcc.Graph(id='graph2', figure=fig_bar, style={'width': '100%', 'height': '100%'})
        ]),
    ]),

    html.Div(className='row', style={'display': 'flex', 'justifyContent': 'center', 'marginTop': '20px'}, children=[
        html.Div(className='six columns', style={'margin-right': '10px', 'border-radius': '10px'}, children=[
            dcc.Graph(id='graph3', figure=fig_scatter, style={'width': '100%', 'height': '100%'})
        ]),
        html.Div(className='six columns', style={'margin-left': '10px', 'border-radius': '10px'}, children=[
            dcc.Graph(id='graph4', figure=fig_pie, style={'width': '100%', 'height': '100%'})
        ]),
    ]),

    # Tabela de Dados
    html.Div(className='row', style={'marginTop': '40px'}, children=[
        html.Div(className='twelve columns', style={'position': 'relative', 'width': '53.5%', 'margin': '0 auto'}, children=[
            html.H2('Base de Dados Exemplo', style={'textAlign': 'center', 'color': cores_graficos['text'], 'marginBottom': '20px'}),
            dash_table.DataTable(
                id='tabela-dados',
                columns=[{'name': col, 'id': col} for col in df.columns],
                data=df.to_dict('records'),
                style_table={'overflowX': 'auto', 'width': '100%'},
                style_header={'backgroundColor': '#444444', 'fontWeight': 'bold', 'border': f'1px solid {cores_graficos["border_color"]}'},
                style_cell={'backgroundColor': '#333333', 'color': cores_graficos['text'], 'border': f'1px solid {cores_graficos["border_color"]}'},
                page_size=10,
                sort_action='native',
                filter_action='native'
            )
        ])
    ]),
])

# Execução do aplicativo Dash
if __name__ == '__main__':
    app.run_server(debug=True)
