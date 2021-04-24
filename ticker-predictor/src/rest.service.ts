import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http : HttpClient) { }

  baseUrl : string = "http://127.0.0.1:5000";

  getLinearReg(ticker:string, mentions:number){
    let params = new HttpParams();
    params = params.append('ticker', ticker);
    params = params.append('mentions', mentions.toString());

    return this.http.get(this.baseUrl + "/linearreg", {params: params});
  }

  getKeras(ticker:string, mentions:number){
    let params = new HttpParams();
    params = params.append('ticker', ticker);
    params = params.append('mentions', mentions.toString());

    return this.http.get(this.baseUrl + "/keras", {params: params});
  }
}
