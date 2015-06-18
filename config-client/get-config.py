import os
import sys
import json
import urllib2

def main():
	appinfo = get_application_info()
	examine_vcap_services(appinfo)

# Get Application Info
#
# Certain information about the application is used in
# the query to the configuration servers, to allow them
# to return config values dependent on the application
# instance deployment
#
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
	json.dump(service, sys.stderr, indent=4)
	print >> sys.stderr
	url = service.get('credentials',{}).get('url')
	if url == None:
		print >> sys.stderr, "services of type spring-config-server must specify a url"
		return
	url += "/" + appinfo['name']
	url += "/" + appinfo['profile']
	config = json.load(urllib2.urlopen(url))
	json.dump(config, sys.stderr, indent=4)
	print >> sys.stderr
	#
	# We iterate through the list in reversed order, as it looks like the
	# Spring Cloud Config Server always returns the most specific context
	# first. So this order leads to the correct merge result if the same
	# property appears in multiple contexts.
	#
	for sources in reversed(config.get('propertySources', [])):
		for key, value in sources.get('source', {}).items():
			print key.replace('.', '_'), value

def get_archaius_config(service, appinfo):
	print >> sys.stderr, "archaius-config:"
	json.dump(service, sys.stderr, indent=4)
	print >> sys.stderr

def get_zuul_config(service, appinfo):
	print >> sys.stderr, "zuul-config:"
	json.dump(service, sys.stderr, indent=4)
	print >> sys.stderr

if __name__ == '__main__':
	main()