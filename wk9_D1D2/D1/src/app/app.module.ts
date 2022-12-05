import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BusinessesComponent } from './businesses.component';

import { WebService } from './web.service';
import { HttpClientModule } from '@angular/common/http';

import { RouterModule } from '@angular/router'
import { HomeComponent } from './home.component';

var routes: any = [
  {
    path: '', 
    component: HomeComponent
  }, 
  {
    path: 'businesses', 
    component: BusinessesComponent
  }
]

@NgModule({
  declarations: [
    AppComponent, BusinessesComponent, HomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule, 
    HttpClientModule, 
    RouterModule.forRoot(routes)
  ],
  providers: [WebService],
  bootstrap: [AppComponent]
})
export class AppModule { }
