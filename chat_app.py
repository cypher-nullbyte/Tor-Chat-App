import datetime
import PySimpleGUI as sg
from tor_query import TorQuery
from stem.control import Controller
import asyncio
import stem

SOCKS_PORT = 9050
SEP = '-$$-$$-'
LINE_B = '-@@-@@-'


def update_talk(talk):
    talk_to_print = []
    for line in talk:
        if line:
            time, user, message = line.split(SEP)
            time = time.split('.')[0]
            time = time[:-3]
            time = ''.join(time)
            talk_to_print.append('[%s] %s: %s' % (time, user, message))
    window.Element('_OUTPUT_').Update('\n'.join(talk_to_print))


def send():
    message = values['_IN_']
    route = 'user/%s/message/%s' % (user, message)
    talk_string = tor_query.query(route)
    talk = talk_string.split(LINE_B)
    update_talk(talk)


def update():
    talk_string = tor_query.query()
    talk = talk_string.split(LINE_B)
    update_talk(talk)


if __name__ == '__main__':

    # SOCKS_PORT = int(input("Tor port: "))

    try:
        tor_process = stem.process.launch_tor_with_config(
            config={
                'SocksPort': str(SOCKS_PORT),
            },
        )
    except:
        print(' * Tor might be already running \n')

    controller = Controller.from_port()
    controller.authenticate()

    socks_port = SOCKS_PORT
    hidden_service_id = input("hidden service id: ")
    hidden_service_auth = input("hidden service authentication key: ")

    controller.set_conf('HidServAuth', '%s.onion %s' % (hidden_service_id, hidden_service_auth))

    user = input("Your user: ")

    domain = hidden_service_id + '.onion'

    tor_query = TorQuery(domain, socks_port)

    talk = []
    layout = [
        [sg.Multiline('', size=(45, 15), key='_OUTPUT_')],
        [sg.Input(do_not_clear=True, key='_IN_'), sg.Button('Send')]
    ]

    window = sg.Window('Tor Chat', layout)
    loop = asyncio.get_event_loop()
    update()

    while True:
        event, values = window.Read(timeout=6000)
        if event == 'Send':
            send()
        elif event == '__TIMEOUT__':
            update()
        elif event is None or event == 'Exit':
            break

    window.Close()
