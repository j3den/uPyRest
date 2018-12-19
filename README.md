# uPyRest
A web server for Micro Python -> ESP32

## Introduction

This is a framework for the ESP32. It provides a confgiuration file based
setup for a simple RESTful web service.

A `config.json` file is placed in the root directory and the installer run
to set up the device.

## Configuration

Example `configuration.json`:

```json
{
	"wifiSettings": {
		"ssid": "PLUSNET-SSID",
		"password": "MYROUTERPASSWORD"
	},

	"webServer": {
		"port": 80
	},

	"Database": {
		"Settings": {
			"databasename": "db"
		}
	},
	"Models": {
		"User": {
			"columns": ["username", "password", "role"]
		},
		"Message": {
			"columns": ["message", "datesent", "userid"]
		}
	},
	"Display":{
		"ssd1306" : true,
		"scl_pin":15,
		"sda_pin":4,
		"oled_reset_pin":16,
		"width":128,
		"height":64
	}
}

```

