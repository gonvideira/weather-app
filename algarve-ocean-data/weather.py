"""Application that retrieves and stores new data"""
import weather_functions as wf

URL_MAP = {
    'HEIGHT': (
        "https://www.hidrografico.pt/json/boia.graph.php?id_est=1005&"
        "id_eqp=1009&gmt=GMT&dtz=Europe/Lisbon&dbn=monican&par=1&per=2"
    ),
    'PERIOD': (
        "https://www.hidrografico.pt/json/boia.graph.php?id_est=1005&"
        "id_eqp=1009&gmt=GMT&dtz=Europe/Lisbon&dbn=monican&par=2&per=2"),
    'DIRECTION': (
        "https://www.hidrografico.pt/json/boia.graph.php?id_est=1005&"
        "id_eqp=1009&gmt=GMT&dtz=Europe/Lisbon&dbn=monican&par=3&per=2"),
    'TEMPERATURE': (
        "https://www.hidrografico.pt/json/boia.graph.php?id_est=1005&"
        "id_eqp=1009&gmt=GMT&dtz=Europe/Lisbon&dbn=monican&par=4&per=2")
}

weather_data = wf.retrieve_data(URL_MAP)
