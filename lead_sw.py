from wsgiref.simple_server import make_server
import RPi.GPIO as GPIO
import time
import json

LEAD_SW = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEAD_SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def is_opened():
  return GPIO.input(LEAD_SW) == GPIO.HIGH
def app(environ, start_response):
  status = '200 OK'
  headers = [
    ('Content-type', 'application/json; charset=utf-8'),
    ('Access-Control-Allow-Origin', '*'),
  ]
  start_response(status, headers)
  return [json.dumps({'opened': is_opened()}).encode("utf-8")]

with make_server('', 3005, app) as httpd:
  print("Serving on port 3005...")
  httpd.serve_forever()
