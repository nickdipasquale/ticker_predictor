import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

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

  constructor() { }

  ngOnInit(): void {
  }

}
