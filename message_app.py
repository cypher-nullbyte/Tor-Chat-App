import datetime
import PySimpleGUI as sg
from tor_query import TorQuery


SEP = '-$$-$$-'


def send():
    print(values['_IN_'])
    message = values['_IN_']
    time = str(datetime.datetime.now())
    talk.append(SEP.join([time, user, message]))
    window.Element('_OUTPUT_').Update(values['_IN_'])


def update():
    print('update')
    window.Element('_OUTPUT_').Update(values['_IN_'])


if __name__ == '__main__':
    socks_port = int(input("Tor controller port: "))
    hidden_service_id = input("hidden service id: ")
    user = input("Your user: ")

    domain = hidden_service_id + '.onion'

    tor_query = TorQuery(domain, socks_port)

    talk = []
    layout = [
        # [sg.Text('', size=(15, 10), key='_OUTPUT_')],
        [sg.Multiline('', size=(45, 10),key='_OUTPUT_')],
        [sg.Input(do_not_clear=True, key='_IN_'), sg.Button('Send')]
    ]

    window = sg.Window('Tor Chat', layout)

    while True:
        event, values = window.Read(timeout=500)
        print(event, values)
        if event == 'Send':
            send()
        elif event == '__TIMEOUT__':
            update()
        elif event is None or event == 'Exit':
            break

    window.Close()
