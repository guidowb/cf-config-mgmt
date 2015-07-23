package main

import (
	"os"
	"sort"
	"net/http"

	"code.google.com/p/gorest"
)

func main() {
	gorest.RegisterService(new(ConfigService))
	http.Handle("/", gorest.Handle())
	http.ListenAndServe(":"+os.Getenv("PORT"), nil)
}

type ConfigService struct {
	gorest.RestService
	environment gorest.EndPoint `method:"GET" path:"/env" output:"[]string"`
}

func (svc ConfigService) Environment() []string {
	properties := os.Environ()
	sort.Strings(properties)
	return properties
}
