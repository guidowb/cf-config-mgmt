import os
import sys
import json
import urllib2

# Because we are running in the context of a container,
# the only way to report back status is to pass it on to
# the application. So we capture all meta-data about our
# attempt to initialize config in a special environment
# variable
config_info = {}

def main():
	appinfo = get_application_info()
	examine_vcap_services(appinfo)

# Get Application Info
#
# Certain information about the application is used in
# the query to the configuration services, to allow them
# to return config values dependent on the application
# instance deployment
def get_application_info():
	appinfo = {}
	vcap_application = json.loads(os.getenv('VCAP_APPLICATION', '{}'))
	appinfo['name'] = vcap_application.get('application_name')
	if appinfo['name'] == None:
		print >> sys.stderr, "VCAP_APPLICATION must specify application_name"
		sys.exit(1)
	appinfo['profile'] = vcap_application.get('space_name', 'default')
	return appinfo

# Query Configuration Services
# 
# We only read configuration from bound config services that
# are appropriately tagged. And since, for user-provided services,
# tags can only be set inside the credentials dict, not in the
# top-level one, we check for tags in both places.
#
def examine_vcap_services(appinfo):
	vcap_services = json.loads(os.getenv('VCAP_SERVICES', '{}'))
	for service in vcap_services:
		service_instances = vcap_services[service]
		for instance in service_instances:
			tags = instance.get('tags', []) + instance.get('credentials',{}).get('tags',[])
			if 'spring-config-server' in tags:
				get_spring_cloud_config(instance, appinfo)
			if 'archaius-config-server' in tags:
				get_archaius_config(instance, appinfo)
			if 'zuul-config-server' in tags:
				get_zuul_config(instance, appinfo)

def get_spring_cloud_config(service, appinfo):
	print >> sys.stderr, "spring-cloud-config:"
	print >> sys.stderr, service
	url = service.get('credentials',{}).get('url')
	if url == None:
		print >> sys.stderr, "services of type spring-config-server must specify a url"
		return
	url += "/" + appinfo['name']
	url += "/" + appinfo['profile']
	config = json.load(urllib2.urlopen(url))
	print config

def get_archaius_config(service, appinfo):
	print >> sys.stderr, "archaius-config:"
	print >> sys.stderr, service

def get_zuul_config(service, appinfo):
	print >> sys.stderr, "zuul-config:"
	print >> sys.stderr, service

def print_error(err):
	sys.stderr.write(err + '\n')

if __name__ == '__main__':
	main()