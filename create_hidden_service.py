from stem.control import Controller
import stem

SOCKS_PORT = 9050

try:
    tor_process = stem.process.launch_tor_with_config(
        config={
            'SocksPort': str(SOCKS_PORT),
        },
    )
except:
    print(' * Tor might be already running')

controller = Controller.from_port()

controller.authenticate()

hidden_services = controller.list_ephemeral_hidden_services()

print(' * Closing any existing hidden services...')

for hidden_service_id in hidden_services:
    print(' * Closing hidden service: %s', hidden_service_id)
    controller.remove_hidden_service(hidden_service_id)

print(' * Initiating a new hidden service')

hidden_service = controller.create_ephemeral_hidden_service(
    {80: 5000},
    await_publication=True,
    basic_auth={'user': None}
)

print(' * Hidden service initialized with id %s' % hidden_service.service_id)
print(' * Hidden service authentication key is %s' % hidden_service.client_auth['user'])
print(' * Controller is listening on port %s' % controller.get_socks_listeners()[0][1])

controller.set_conf('HidServAuth', '%s.onion %s' % (hidden_service.service_id, hidden_service.client_auth['user']))
