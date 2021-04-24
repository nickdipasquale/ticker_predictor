import { NONE_TYPE } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { $ } from 'protractor';
import { error } from 'selenium-webdriver';
import { RestService } from '../../rest.service';

@Component({
  selector: 'app-method',
  templateUrl: './method.component.html',
  styleUrls: ['./method.component.css']
})
export class MethodComponent implements OnInit {

  constructor(private rs: RestService) { }

  loading = false;
  ticker: string = "";
  mentions!: number;
  prediction: string = "";
  impliedv: string = "";
  current_price: string = "";
  prediction_low: string = "";
  prediction_high: string = "";
  stock_info: string = "";

  getKMPrediction(ticker: string, mentions: number) {
    this.rs.getKeras(ticker, mentions)
      .subscribe
      (
        (response) => {
          var json = JSON.parse(JSON.stringify(response))
          
          this.prediction = json.prediction;
          this.impliedv = json.impliedv;
          this.current_price = json.price;
          this.prediction_low = json.prediction_low;
          this.prediction_high = json.prediction_high;
          this.stock_info = json.stock_info;
          this.loading = false;

          document.getElementById("pc")?.removeAttribute("hidden");
          document.getElementById("cp")?.removeAttribute("hidden");
          document.getElementById("pp")?.removeAttribute("hidden");
          document.getElementById("iv")?.removeAttribute("hidden");
          document.getElementById("pc1")?.removeAttribute("hidden");
          document.getElementById("pc2")?.removeAttribute("hidden");
          document.getElementById("pc3")?.removeAttribute("hidden");
          document.getElementById("pp1")?.removeAttribute("hidden");
          document.getElementById("pp2")?.removeAttribute("hidden");
          document.getElementById("pp3")?.removeAttribute("hidden");
        },
        (error)=>{
          this.prediction = "Invalid Ticker";
          this.loading = false;
        }
      )
  }

  ngOnInit(): void { }

  generatePrediction() {
    this.loading = true;
    this.getKMPrediction(this.ticker, this.mentions)
  }
}
