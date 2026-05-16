from client.network import connect_to_relay

def test_connection():
    assert connect_to_relay is not None
