from vm_client import vmclient
import numpy as np
import sys


def filter_labels(raw_labels: list,keyword: str) -> list:
    print('filtering labels...')
    filtered_labels = [label for label in raw_labels if label.startswith(keyword.lower())]
    return filtered_labels

def create_payload() -> str:
    data_type = ['vim','nfvi']
    environment = ['zagt5','zgt4','zagt6','zagt7','zagt8','zagt9','zagt10']
    title = ['benchmark2test','benchmark3test','benchmark4test','benchmark5test']
    test_suite = ['l2_tests','l3_tests','l4_tests','l5_tests']
    test_name = ['network_check','network_check2','network_check3','network_check4','network_check5']
    kpi_name = ['p1','p2','p3','p4','p5']
    value = [4.2,43.1,50.3,90.5]
    env = np.random.choice(environment)
    kpi = np.random.choice(kpi_name)
    val = float(np.random.choice(value))


    # tags: environment, test_name, test_suite, data_type
    # fields: title (string), KPI as numeric field key
    title = np.random.choice(title)
    try:
        print('creating payload for {}'.format(env))
        line = (
        f"touchstone,environment={env},test_name={np.random.choice(test_name)},"
        f"test_suite={np.random.choice(test_suite)},data_type={np.random.choice(data_type)} "
        f'title="{title}",{kpi}={val}'
        )
        return line
    except:
        print('failed to create payload')
        return ''
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        print('Creating VM client...')
        vmclient.write_data(create_payload())
        print('success')
    except Exception as e:
        print(f'failed to create payload: {e}')
        sys.exit(1)

    print('returning new labels...')
    labels = vmclient.get_labels()
    print(labels)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
