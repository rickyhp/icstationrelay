# -*- coding: utf-8 -*-

from waitress import serve
import relay_flask

serve(relay_flask.app, host='0.0.0.0', port=8080)