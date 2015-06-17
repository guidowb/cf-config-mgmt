package main

import (
	"os"
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

func (svc ConfigService) Environment() (env []string) {
	env = os.Environ()
	return
}