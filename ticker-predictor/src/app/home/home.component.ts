import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { RestService } from '../../rest.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private rs: RestService) { }

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

  selectedStockControl = new FormControl()

  prediction: string = "";

  getPrediction(ticker:string) {
    this.rs.getPrediction(ticker)
      .subscribe
      (
        (response) => {
          this.prediction = response.toString();
          this.setPrediction(+response.toString());
        }
      )
  }

  ngOnInit(): void {
    this.selectedStockControl.valueChanges.subscribe(value => {
      this.getPrediction(value);
    })
  }

  setPrediction(value: number) {
    var textField = document.getElementById("prediction");
    this.prediction = value.toString();

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
}
