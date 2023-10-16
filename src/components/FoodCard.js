import React from 'react'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
//import Photo from '../photos/logo192.png'
import {  Link } from "react-router-dom"
import FoodData from "../components/data/NewRecipe.json"
import PonzuPhoto from "../components/photos/ponzu.jpg"

// const FoodPhoto = (photoSource) => {
//   if(FoodData.food.recipeName == "Ponzu"){
//     photoSource = PonzuPhoto
//   }
//   else {
//     photoSource = Photo
//   }

// }

function FoodCard({name, cuisine}) {
  var source = ""
  //FoodPhoto(source)
  return (
    <Card style={{ width: '18rem' }}>
    <Card.Img variant="top" src={PonzuPhoto} /> 
    <Card.Body>
      <Card.Title>{name}</Card.Title>
      <Card.Text>
        {cuisine}
      </Card.Text>
      <Link to = '/home'>
      <Button variant="success">See Recipe</Button> 
       {/* onClick={() => console.log('Hello')}  */}
      </Link>
    </Card.Body>
  </Card>
  )
}

export default FoodCard