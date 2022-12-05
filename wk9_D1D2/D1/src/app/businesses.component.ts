import { Component } from '@angular/core';
import { WebService } from './web.service';

@Component({
  selector: 'businesses',
  templateUrl: './businesses.component.html',
  styleUrls: ['./businesses.component.css']
})

export class BusinessesComponent {
  business_list : any;

  constructor(public webService: WebService) {}

  ngOnInit() {
    this.webService.getBusinesses();
  }
}