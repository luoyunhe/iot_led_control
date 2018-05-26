# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.username_pw_set("admin", "password")
HOST = "120.77.183.4"


def led_on(request):
    client.connect(HOST, 1883, 60)
    client.publish("726iot_mqtt_led", '1')
    client.disconnect()
    return render(request, 'lamp_on.html')


def led_off(request):
    client.connect(HOST, 1883, 60)
    client.publish("726iot_mqtt_led", '0')
    client.disconnect()
    return render(request, 'lamp_off.html')

