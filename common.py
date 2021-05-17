import json
import time
import datetime

def export_to_json(material, json_file):
    output = json.dumps(material, indent=4, ensure_ascii=False)
    op = open(json_file, 'w', encoding="utf-8")
    op.write(output)
    op.close()

def load_from_json(json_file):
    op = open(json_file, 'r')
    data = op.read()
    dic = json.loads(data)
    return dic

def timestring_handle(timestring):
    today = datetime.date.today()
    now = datetime.datetime.now()
    result = {"from": "", "to": "", "api_from": "", "api_to": ""}

    if timestring == "Yesterday":
        preset = today - datetime.timedelta(days=1)
        result["from"] = preset.strftime("%B %d, %Y")
        result["to"] = result["from"]
        result["api_from"] = "now-1d"
        result["api_to"] = "now-1d"

    if timestring == "Today":
        preset = today
        result["from"] = preset.strftime("%B %d, %Y")
        result["to"] = result["from"]
        result["api_from"] = "now-0d"
        result["api_to"] = "now"

    if timestring == "Last 30 minutes":
        preset = now - datetime.timedelta(minutes=30)
        result["from"] = preset.strftime("%B %d, %Y %H:%M")
        result["to"] = now.strftime("%B %d, %Y %H:%M")
        result["api_from"] = "now-30m"
        result["api_to"] = "now"

    if timestring == "Last 1 hour":
        preset = now - datetime.timedelta(hours=1)
        result["from"] = preset.strftime("%B %d, %Y %H:%M")
        result["to"] = now.strftime("%B %d, %Y %H:%M")
        result["api_from"] = "now-1h"
        result["api_to"] = "now"

    if timestring == "Last 2 hours":
        preset = now - datetime.timedelta(hours=2)
        result["from"] = preset.strftime("%B %d, %Y %H:%M")
        result["to"] = now.strftime("%B %d, %Y %H:%M")
        result["api_from"] = "now-2h"
        result["api_to"] = "now"

    if timestring == "Last 6 hours":
        preset = now - datetime.timedelta(hours=6)
        result["from"] = preset.strftime("%B %d, %Y %H:%M")
        result["to"] = now.strftime("%B %d, %Y %H:%M")
        result["api_from"] = "now-6h"
        result["api_to"] = "now"

    if timestring == "Last 24 hours":
        preset = now - datetime.timedelta(hours=24)
        result["from"] = preset.strftime("%B %d, %Y %H:%M")
        result["to"] = now.strftime("%B %d, %Y %H:%M")
        result["api_from"] = "now-24h"
        result["api_to"] = "now"

    if timestring == "Last 72 hours":
        preset = now - datetime.timedelta(hours=72)
        result["from"] = preset.strftime("%B %d, %Y %H:%M")
        result["to"] = now.strftime("%B %d, %Y %H:%M")
        result["api_from"] = "now-72h"
        result["api_to"] = "now"

    if timestring == "Last 7 days":
        preset = today - datetime.timedelta(days=1)
        result["from"] = preset.strftime("%B %d, %Y %H:%M")
        result["to"] = now.strftime("%B %d, %Y %H:%M")
        result["api_from"] = "now-7d"
        result["api_to"] = "now"

    if timestring == "Last 30 days":
        preset = today - datetime.timedelta(days=30)
        result["from"] = preset.strftime("%B %d, %Y %H:%M")
        result["to"] = now.strftime("%B %d, %Y %H:%M")
        result["api_from"] = "now-30d"
        result["api_to"] = "now"

    return result

def timestamp_handle(timestring_from, timestring_to):
    def convert_to_timestamp(timestring):
        date_object = datetime.datetime.strptime(timestring,"%d/%m/%Y %H:%M")
        new_format = date_object.strftime("%B %d, %Y %H:%M")
        timestamp = int(time.mktime(date_object.timetuple())) * 1000
        return [timestamp, new_format]
    time_from = convert_to_timestamp(timestring_from)
    time_to = convert_to_timestamp(timestring_to)
    result = {
        "from": time_from[1],
        "to": time_to[1],
        "api_from": time_from[0],
        "api_to": time_to[0]
    }
    return result
