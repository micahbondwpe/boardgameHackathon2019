import React, {Component} from "react"
import axios from "axios"
import queryString from 'query-string'
import "../css/style.css"

class Boardgame extends Component {
    constructor() {
        super()
        this.state = {
        }
    }

    componentDidMount() {
        const values = queryString.parse(this.props.location.search)
        console.log(values.id)
        axios.get(`http://localhost:5000/boardgame/${values.id}`).then(response => {
            this.setState({ 
                "age": response.data.age,
                "boardgamecategory": response.data.boardgamecategory,
                "boardgamemechanic": response.data.boardgamemechanic, 
                "id": response.data.id, 
                "image": response.data.image, 
                "maxplayers": response.data.maxplayers, 
                "minplayers": response.data.minplayers, 
                "name": response.data.name, 
                "playingtime": response.data.playingtime, 
                "rating": response.data.rating, 
                "thumbnail": response.data.thumbnail
            });
        });
      }
    render() {
        return(
            <div>
                <h2>{this.state.name}</h2>
                <img src={this.state.thumbnail} alt={this.state.name}></img>
                <p>Rating: {this.state.rating}</p>
                <p>Players: {this.state.minplayers} - {this.state.maxplayers}</p>
                <p>Average Playtime: {this.state.playingtime}</p>
                <p>Minimum Age: {this.state.age}</p>
            </div>
        )
    }
}



export default Boardgame