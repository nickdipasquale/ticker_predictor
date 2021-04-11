import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor() { }

  stocks: string[] = [
    "GME",
    "SPY",
    "TSLA",
    "PLTR",
    "AAPL",
    "AMC",
    "RKT",
    "NIO",
    "DIS",
    "BB",
    "AMD",
    "ARKK",
    "DASH",
    "QQQ",
    "RBLX",
    "TLRY",
    "APHA",
    "BA",
    "MVIS",
    "NOK",
    "SNDL",
    "APPL",
    "PLUG",
    "GOEV",
    "ET",
    "GLD",
    "UPST",
    "INTC",
    "CRSR",
    "VIAC",
    "FUBO",
    "ROOT",
    "BIDU"
  ];


  ngOnInit(): void {
  }

  setPrediction(value: number) {
    var textField = document.getElementById("prediction");

    if (textField != null) {
      textField.innerHTML = value.toString() + "%";

      if (value > 0) {
        textField.classList.remove("positive");
        textField.classList.remove("negative");
        textField.classList.remove("zero");
        textField.classList.add("positive");
      }
      else if (value < 0) {
        textField.classList.remove("positive");
        textField.classList.remove("negative");
        textField.classList.remove("zero");
        textField.classList.add("negative");
      }
      else if (value == 0) {
        textField.classList.remove("positive");
        textField.classList.remove("negative");
        textField.classList.remove("zero");
        textField.classList.add("zero");
      }
    }
  }

  predictionValue: string = "0";

  selectedStockControl = new FormControl(this.predictionValue)

}
