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
            html.H1('A single column'),
            dbc.Tabs(
                [
                    dbc.Tab([
                        dbc.Row(
                            [
                                dbc.Col(html.Div([
                                    html.H3('Column one of the first tab'),
                                    html.Ul([
                                        html.Li('First'),
                                        html.Li('Second'),
                                        html.Li('Third'),
                                    ])
                                ])),
                                dbc.Col(html.Div([
                                    html.H3('Column two of the first tab'),
                                    html.Ul([
                                        html.Li('Первый'),
                                        html.Li('Второй'),
                                        html.Li('Третий'),
                                    ])
                                ])),
                            ]
                        )
                    ], label="Tab-1", tab_id="tab-1"),
                    dbc.Tab([
                        html.H3('Column of the second tab'),
                        html.Ul([
                            html.Br(),
                            html.Li('Number of Economies'),
                            html.Li('Temporal Coverage'),
                            html.Li('Updte Frequency'),
                        ])
                    ], label="Tab-2", tab_id="tab-2"),
                ]
            )
        ]))),
        # dbc.Row(
        #     [
        #         dbc.Col(html.Div([
        #             html.H1("The last of tree columns"),
        #             html.Ul([
        #                 html.Li('Number of Economies'),
        #                 html.Li('Templral Coverage'),
        #                 html.Li('Update Rrequency'),
        #             ])
        #         ]), width={"size": 3, "order": "last", "offset": 1}),
        #         dbc.Col(html.Div([
        #             html.H1("The first of tree columns"),
        #             html.Ul([
        #                 html.Li('Number of Economies'),
        #                 html.Li('Templral Coverage'),
        #                 html.Li('Update Rrequency'),
        #             ])
        #         ]), width={"size": 3, "order": 1, "offset": 2}),
        #         dbc.Col(html.Div([
        #             html.H1("The second of tree columns"),
        #             html.Ul([
        #                 html.Li('Number of Economies'),
        #                 html.Li('Templral Coverage'),
        #                 html.Li('Update Rrequency'),
        #             ])
        #         ]), width={"size": 3, "order": 5}),
        #     ]
        # )
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
    
