import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable()
export class WebService{
    constructor(private http: HttpClient){}

    business_list: any;

    getBusinesses() {
        return this.http.get(
            'http://localhost:5000/api/v1.0/businesses'
        ).subscribe((response: any) => {
            this.business_list = response;
            console.log(response)
        })
    }
}