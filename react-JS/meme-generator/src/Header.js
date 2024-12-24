import React from "react"

function Header() {
    return (
        <header className="d-flex flex-column align-items-center py-3 mb-4 border-bottom">
            <img
                src="http://www.pngall.com/wp-content/uploads/2016/05/Trollface.png"
                alt="Problem?"
                height="64"
                className="mb-2"
            />
            <p className="fs-1 fw-bold mb-0">Meme Generator</p>
        </header>
    )
}

export default Header