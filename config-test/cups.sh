#!/bin/sh

cf delete-service -f spring-config-server
cf delete-service -f archaius-config-server
cf delete-service -f zuul-config-server

cf cups spring-config-server -p '{"url":"http://spring-cloud-config-server.10.244.0.34.xip.io","tags":["spring-config-server"]}'
cf cups archaius-config-server -p '{"url":"http://archaius-config-server.10.244.0.34.xip.io","tags":["archaius-config-server"]}'
cf cups zuul-config-server -p '{"url":"http://zuul-config-server.10.244.0.34.xip.io","tags":["zuul-config-server"]}'
