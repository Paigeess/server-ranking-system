from requests import get,post,Request

class VmClient:
    HOST_NAME_URL = 'http://127.0.0.1:8428/'
    LABELS = 'api/v1/labels'
    METRICS = 'api/v1/label/__name__/values'
    METRICS_META = 'api/v1/series?match[]={metric}{filter}&start=-365d'
    LABEL_VALUES = 'api/v1/label/{label_name}/values?start={start}&end={end}'
    SERIES = 'api/v1/query?query={metric}{filter}&start={start}&end={end}'


    def __init__(self):
        return

    def get_labels(self) -> list:
            response = get(f'{self.HOST_NAME_URL}{self.LABELS}',verify=False)
            response.raise_for_status()
            print(f'getting request from url: {self.HOST_NAME_URL}{self.LABELS}')
            return response.json().get('data',[])

    def write_data(self,payload):
        formatted_data = '\n'.join(payload)
        response = post(f'{self.HOST_NAME_URL}{self.LABELS}',data=formatted_data,verify=False)
        response.raise_for_status()

