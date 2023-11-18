# Импорты:
from dash import Dash, html

# Создание экземпляра приложения:
app = Dash(__name__)


# Макет приложения
app.layout = html.Div([
    html.H1('Poverty And Equity Database',
        style={
            'color': 'blue',
            'fontSize': '40px',
            }),
    html.H2('The World Bsnk'),
    html.P('Key Facts'),
    html.Ul([
        html.Li('Number of Economies: 170'),
        html.Li('Templral Coverage: 1974 - 2019'),
        html.Li('Update Frequency: Quartely'),
        html.Li('Last Updated: March 18, 2020'),
        html.Li([
            'Source: ',
            html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',\
                   href='https://datacatalog.wordlbank.org/dataset/poverty-and-equity-database')
        ])
    ])
])


# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
    
