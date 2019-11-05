import React, {Component} from "react"
//import axios from "axios"
import queryString from 'query-string'

class Boardgame extends Component {
    constructor() {
        super()
        this.state = {
        }
    }

    componentDidMount() {
        const values = queryString.parse(this.props.location.search)
        console.log(values.id)
      }
    render() {
        return(
            <div>
                
            </div>
        )
    }
}



export default Boardgame