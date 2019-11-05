import React from "react"
import "../css/nav.css"

function Nav() {
    return(
        <div>
            <nav>
                <ul>
                    <li><a href="/">Homepage</a></li>
                    <li><a href="/login">Login</a></li>
                </ul>
            </nav>
        </div>
    )
}

export default Nav