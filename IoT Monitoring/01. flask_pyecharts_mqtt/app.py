from random import randrange

from flask.json import jsonify
from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Line
import paho.mqtt.client as mqtt
import re

import threading
from threading import Thread
import time

app = Flask(__name__, static_folder="templates");
idx = 9;
currTemp=25;
	
def line_base() -> Line:
	line = (
		Line()
		.add_xaxis(["{}".format(i) for i in range(10)])
		.add_yaxis(
			series_name="",
			y_axis=[currTemp for _ in range(10)],
			is_smooth=True,
			label_opts=opts.LabelOpts(is_show=False),
		)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="Monitor"),
			xaxis_opts=opts.AxisOpts(type_="value"),
			yaxis_opts=opts.AxisOpts(type_="value"),
		)
	)
	return line

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/lineChart")
def get_line_chart():
	c = line_base()
	return c.dump_options_with_quotes()

@app.route("/lineDynamicData")
def update_line_data():
	global idx
	global currTemp
	idx = idx + 1
	return jsonify({"name": idx, "value": currTemp})

def on_connect(mqttc, obj, flags, rc):
	print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
	global currTemp
	text = str(msg.payload);
	print(text);
	match_result = re.match(r'b\'h:([0-9\.]+) t:([0-9\.]+)', text);
	print(match_result);
	print(match_result.group(1))
	print(match_result.group(2))
	currTemp = float(match_result.group(2));
	print("incoming message " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mqttc, obj, mid):
	print("mid: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
	print(string)

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print("Starting " + self.name)
		if self.threadID==1 :
			app.run();
		else:
			mqttc.loop_forever()

# init mqtt client parameters.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Modify the following IP and subscribe topic by your environment.
mqttc.connect("192.168.1.120", 1883, 60)
mqttc.subscribe("Try/MQTT/Docker", 0)

# Create new threads
# Thread for flask
thread1 = myThread(1, "Thread-flask", 1)
# Thread for mqtt
thread2 = myThread(2, "Thread-mqtt", 2)

# Start new Threads
thread1.start()
thread2.start()
