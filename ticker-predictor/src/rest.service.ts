import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http : HttpClient) { }

  stockUrl : string = "http://127.0.0.1:5000/result";

  getPrediction(ticker:string, mentions:number){
    let params = new HttpParams();
    params = params.append('ticker', ticker);
    params = params.append('mentions', mentions.toString());

    return this.http.get(this.stockUrl, {params: params});
  }
}
