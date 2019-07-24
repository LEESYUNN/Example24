package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
)

type response struct {
    User string `json:"user"`
    Languages []string `json:"languages"`
}

func indexExamplePage(w http.ResponseWriter, r *http.Request) {

    returnJson := &response{
        User: "LEESYUNN",
        Languages: []string{"Chinese", "Korean", "Japanese", "English"}}

    encodedJson, _ := json.Marshal(returnJson)

    fmt.Fprintf(w, string(encodedJson))
}

func main() {

    http.HandleFunc("/", indexExamplePage)

    err := http.ListenAndServe(":8080", nil)

    if err != nil {
        log.Fatal("ListenAndServe: ", err)
    }
}