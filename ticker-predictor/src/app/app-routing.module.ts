import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router'; // CLI imports router
import { HomeComponent } from './home/home.component';
import { DataComponent } from './data/data.component';
import { MethodComponent } from './method/method.component';

const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'method', component: MethodComponent },
    { path: 'data', component: DataComponent },
  ];

// configures NgModule imports and exports
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }