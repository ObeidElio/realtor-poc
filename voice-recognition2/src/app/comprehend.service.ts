import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class ComprehendService {

  

  constructor(private http: HttpClient) {}


  getKeyPhrases(text: string): Observable<any>{
    return this.http.post<any>("http://127.0.0.1:5001/api/v1/comprehend/bot",{"Text":text})
  }
  
  
}
