#!/bin/sh

cf delete-service -f spring-config-server
cf delete-service -f archaius-config-server
cf delete-service -f zuul-config-server

cf cups spring-config-server -p '{"url":"http://spring-cloud-config-server.cfapps.io","tags":["spring-config-server"]}'
cf cups archaius-config-server -p '{"url":"http://archaius-config-server.cfapps.io","tags":["archaius-config-server"]}'
cf cups zuul-config-server -p '{"url":"http://zuul-config-server.cfapps.io","tags":["zuul-config-server"]}'
