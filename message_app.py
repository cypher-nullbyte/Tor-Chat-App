import datetime
import PySimpleGUI as sg
from tor_query import TorQuery
import asyncio


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


@asyncio.coroutine
def send():
    # Update text

    # time = str(datetime.datetime.now())
    # talk.append(SEP.join([time, user, message]))
    # update_talk(talk)

    # Query post message

    message = values['_IN_']
    route = 'user/%s/message/%s' % (user, message)
    talk_string = tor_query.query(route)
    print(talk_string)
    talk = talk_string.split(LINE_B)
    update_talk(talk)

    # return talk


@asyncio.coroutine
def update():
    print('update')
    talk_string = tor_query.query()
    print(talk_string)
    talk = talk_string.split(LINE_B)
    update_talk(talk)

    # return talk


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
    loop = asyncio.get_event_loop()
    while True:
        event, values = window.Read(timeout=500)
        # print(event, values)
        if event == 'Send':
            send()
        elif event == '__TIMEOUT__':
            try:
                # update().send(datetime.datetime.now())
                loop.run_until_complete(update())
            except StopIteration as exe:
                print('executed %s' % exe)
        elif event is None or event == 'Exit':
            break

    window.Close()
