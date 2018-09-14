from unittest.mock import patch

import app.views.index


class MockMD5(object):

    def __init__(self, return_value):
        self._return_value = return_value

    def hexdigest(self):
        return self._return_value


def test_index(client):
    expected_version = "1234567890"
    expected_value = "favicon.ico?version={}".format(expected_version)

    with patch.object(app.views.index, "md5", return_value=MockMD5(expected_version)):
        with open("app/templates/index.html", "rb") as template:
            expected_body = template.read().replace(bytes("{{ icon }}", encoding="utf-8"),
                                                    bytes(expected_value, encoding="utf-8"))
            assert client.get("/").status_code == 200
            assert client.get("/").get_data() == expected_body


def test_favicon(client):
    with open("favicon.ico", "rb") as icon:
        assert client.get("/favicon.ico").status_code == 200
        assert client.get("/favicon.ico").get_data() == icon.read()
