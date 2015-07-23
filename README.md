# cf-config-mgmt
This project demonstrates centralization of management of application settings and properties in Cloud Foundry. By making some very basic buildpack changes, we can inject application properties into the standard environment from bound configuration servers of various types
- Without requiring changes to application code
- For any programming language supported by Cloud Foundry
- For any configuration server type

The demo shows this for two languages (Golang and Python), and two configuration server types (Spring Cloud Config and Zuul), but the approach is easily extensible to other languages and server types.

## Forked Buildpacks

The approach demonstrated here requires changes to the buildpacks for the supported languages to inject the configuration client utility into the .profile.d directory of the application containers. The forked buildpacks for Golang and Python with those changes are here:
- [Modified Golang buildpack](http://github.com/guidowb/go-buildpack)
- [Modified Python buildpack](http://github.com/guidowb/buildpack-python)

