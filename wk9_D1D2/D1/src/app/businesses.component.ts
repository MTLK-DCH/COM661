import { Component } from '@angular/core';

@Component({
  selector: 'businesses',
  templateUrl: './businesses.component.html',
  styleUrls: ['./businesses.component.css']
})
export class BusinessesComponent {
  business_list = [
      {
          "name": "Pizza Place", 
          "city": "Coleraine",
          "review_count": 10
      },
      {
        "name": "Wine Lake", 
        "city": "BallMoney",
        "review_count": 7
    },
    {
        "name": "Beer Tavern", 
        "city": "Ballymena",
        "review_count": 12
    },
  ];
}