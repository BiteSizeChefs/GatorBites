import React, { useState } from 'react'
import InputGroup from 'react-bootstrap/InputGroup'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import { Link } from 'react-router-dom'
import FoodCard from "../components/FoodCard"
import FoodData from "../components/data/NewRecipe.json"
import "../components/styles/Search.css"
import Tabs from './TabbedList'

function Search() {
  const [ingInfo, setIngInfo] = useState({ ingredient_1: '' })
  const [Match, setMatch] = useState([])

  const addIngredient = () => {
    const len = Object.keys(ingInfo).length
    const newIng = Object.assign({}, ingInfo)
    newIng[`ingredient_${len + 1}`] = ''
    setIngInfo(newIng)
  }

  const setCurrIngredient = (ingredientProp, ingredientString) => {
    const newIng = Object.assign({}, ingInfo)
    newIng[ingredientProp] = ingredientString
    setIngInfo(newIng)
  }

  const findRecipe = () => {
  var len = FoodData.food.length
  var newFood = []
  for (var i = 0; i < len; i++) {
    let inFood = true
    for (let ingredient in ingInfo) {
        // console.log(ingInfo[ingredient])
      if (!FoodData.food[i].ingredients.includes(ingInfo[ingredient])) {
        // one ingredient does not match
        inFood = false
        break
      }
    }
    if (inFood) newFood.push(FoodData.food[i]) //loads the match correctly but doesnt display them
    //if(inFood) setMatch([...Match, FoodData.food[i]]) //actually lets them show up but theres a duplicate
   
    // if (inFood){
    //   var len = FoodData.food.length
    //   for(var i=0; i<len; i++)
    //   setMatch([...Match, FoodData.food[i]])
    // } 
  }
  setMatch(newFood)
  //console.log(Match)
}

const handleReset = () => {
  Array.from(document.querySelectorAll("input")).forEach(
    input => (input.value = "")
  );
  setMatch([])
  setIngInfo({ingredient_1: ''})
}

  return (
    <>
      {/* <InputGroup.Checkbox aria-label="Checkbox for following text input"  /> */}



      <div className='input'>
      {Object.keys(ingInfo).map((ing, i) => {
        return (
          
          <InputGroup key={i}>
            <Form.Control
              //type="text"
              aria-label='Text input with checkbox'
              placeholder='Ingredient'
              onChange={(e) => setCurrIngredient(ing, e.target.value)}
              value={ing.value}
            />
          </InputGroup>
        )
      })}
      </div>

      <div className='input-buttons'>
      <Button variant='primary' onClick={() => addIngredient()}>
        Add more ingredients
      </Button>
      {/* <Link to='/recipe'> */}
      
      
      
      {/* </Link> */}
      <Button variant='danger'onClick={() => handleReset()}>Clear Query</Button>
      </div>
      <div className='to-recipes'>
      <Button variant='success'onClick={() => findRecipe()}>See my recipes!</Button>
      </div>
      {Match.map(food =><FoodCard name={food.recipeName} cuisine={food.cuisine} />)}
      {Match.map(food =><Tabs name={food.recipeName} cuisine={food.cuisine} />)}
    </>
  )
}

export default Search