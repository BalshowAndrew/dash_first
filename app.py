# Импорты:
from dash import Dash, html, dcc

# Создание экземпляра приложения:
app = Dash(__name__)


# Макет приложения
app.layout = html.Div([
    html.H1('Hello, World')
])


# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
    
