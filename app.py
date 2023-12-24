# Импорты:
from dash import Dash, html
import dash_bootstrap_components as dbc

# Создание экземпляра приложения:
app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]

)


app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div([
            html.H1('A single column')
        ]))),
        dbc.Row(
            [
                dbc.Col(html.Div([
                    html.H1("One of tree columns"),
                    html.Ul([
                        html.Li('Number of Economies'),
                        html.Li('Templral Coverage'),
                        html.Li('Update Rrequency'),
                    ])
                ])),
                dbc.Col(html.Div([
                    html.H1("One of tree columns"),
                    html.Ul([
                        html.Li('Number of Economies'),
                        html.Li('Templral Coverage'),
                        html.Li('Update Rrequency'),
                    ])
                ])),
                dbc.Col(html.Div([
                    html.H1("One of tree columns"),
                    html.Ul([
                        html.Li('Number of Economies'),
                        html.Li('Templral Coverage'),
                        html.Li('Update Rrequency'),
                    ])
                ])),
            ]
        )
    ])

# # Макет приложения
# app.layout = html.Div([
#     html.H1('Poverty And Equity Database'),
#     html.H2('The World Bsnk'),
#     html.P('Key Facts'),
#     html.Ul([
#         html.Li('Number of Economies: 170'),
#         html.Li('Templral Coverage: 1974 - 2019'),
#         html.Li('Update Frequency: Quartely'),
#         html.Li('Last Updated: March 18, 2020'),
#     ])
# ])


# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
    
