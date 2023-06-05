from fastapi import FastAPI
import RPi.GPIO as GPIO

LEAD_SW = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEAD_SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

app = FastAPI()
@app.get("/")
def has_key():
   return {
       "has_key": GPIO.input(LEAD_SW) == GPIO.LOW
   }
