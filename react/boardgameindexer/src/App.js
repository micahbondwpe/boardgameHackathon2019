import React from "react"
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Homepage from "./Pages/Homepage"
import Boardgame from "./Pages/Boardgame"

function App() {
    return(
        <Router>
            <div>
                <Route exact path="/"><Homepage /></Route>
                <Route path="/boardgame" component={Boardgame} />

            </div>
        </Router>
    )
}

export default App