import requests


class PostSender:
    def __init__(self, url):
        self.url = url

    def send_post(self, serial_number, model, coment, company, status):
        data = {
            'serial_number': serial_number,
            'model': model,
            'coment': coment,
            'company': company,
            'status': status
        }

        response = requests.post(self.url, json=data)

        if response.status_code == 200:
            return 'Żądanie POST zostało wysłane poprawnie.'
        else:
            return f'Błąd podczas wysyłania żądania POST. Kod odpowiedzi: {response.status_code}'
