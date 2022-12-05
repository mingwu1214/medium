# How to Build Communication for M2M and IoT using MQTT (Part 1 - MQTT monitor using Flask with pyecharts)

  Message Queuing Telemetry Transport (MQTT) is a publish/subscribe messaging transport protocol. [1]  MQTT is the de facto standard for IoT, and many companies use MQTT in power consumption metering, vehicle communication, and manufacturing. So MQTT is an essential skill we must know.
 Following is a hands-on web-based lab as your first step to familiarize yourself with MQTT temperature monitoring. Flask is an easy-to-use backend, and pyecharts is an easy-to-use visualization library. 
 
(1) The following code was modified from the sample code of pyechart.org/web_flask[2] and eclipse/paho.mqtt.python[3] . 

(2) Ensure the index.html is in "templates/index.html", or the flask may not work well.

(3) add threading for both flask and MQTT procedures, and then they can work parallel. (app.py)

(4) got the MQTT payload using the on_massage function; this payload defined both humidity and temperature. Use regex to get the temperature value of the payload.

(5) Modify the following IP and subscribe topic by your environment.
```python
# Modify the following IP and subscribe topic by your environment.
mqttc.connect("192.168.1.120", 1883, 60)
mqttc.subscribe("Try/MQTT/Docker", 0)
```

(6) Invoke app.py to start the server
```
python app.py
```

## Demo Video
 The temperature values changed by the other MQTT embedded  device. In future articles, you will learn how to send MQTT messages from embedded devices.

[![Everything Is AWESOME](https://img.youtube.com/vi/HLaFPGO8kv4/0.jpg)](https://www.youtube.com/watch?v=HLaFPGO8kv4 "Everything Is AWESOME")
 
## References
[[1] MQTT Specifications ](https://mqtt.org/mqtt-specification/)

[[2] Web Flask+Pyecharts ](https://pyecharts.org/)

[[3] eclipse/paho.mqtt.python](https://github.com/pradeesi/Paho-MQTT-with-Python/blob/master/mqtt_subscribe.py)
