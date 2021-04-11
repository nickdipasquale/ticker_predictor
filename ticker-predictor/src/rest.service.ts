import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http : HttpClient) { }

  stockUrl : string = "http://127.0.0.1:5000/result";

  getPrediction(ticker:string){
    const opts = { params: new HttpParams({fromString: "ticker=" + ticker}) };
    return this.http.get(this.stockUrl, opts);
  }
}
