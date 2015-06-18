#!/bin/sh

VCAP_APPLICATION={\"application_name\":\"foo\",\"space_name\":\"development\"}
VCAP_SERVICES={\"user-provided\":[{\"name\":\"spring-config-server\",\"label\":\"user-provided\",\"tags\":[],\"credentials\":{\"tags\":[\"spring-config-server\"],\"url\":\"http://spring-cloud-config-server.10.244.0.34.xip.io\"},\"syslog_drain_url\":\"\"},{\"name\":\"archaius-config-server\",\"label\":\"user-provided\",\"tags\":[],\"credentials\":{\"tags\":[\"archaius-config-server\"],\"url\":\"http://archaius-config-server.10.244.0.34.xip.io\"},\"syslog_drain_url\":\"\"},{\"name\":\"zuul-config-server\",\"label\":\"user-provided\",\"tags\":[],\"credentials\":{\"tags\":[\"zuul-config-server\"],\"url\":\"http://zuul-config-server.10.244.0.34.xip.io\"},\"syslog_drain_url\":\"\"}]}

export VCAP_SERVICES
export VCAP_APPLICATION

python get-config.py
