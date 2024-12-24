import React, {Component} from "react"

class MemeGenerator extends Component {
    constructor() {
        super()
        this.state = {
            topText: "",
            bottomText: "",
            randomImg: "http://i.imgflip.com/1bij.jpg",
            allMemeImgs: []
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    componentDidMount() {
        fetch("https://api.imgflip.com/get_memes")
            .then(response => response.json())
            .then(response => {
                const {memes} = response.data
                this.setState({ allMemeImgs: memes })
            })
    }

    handleChange(event) {
        const {name, value} = event.target
        this.setState({ [name]: value })
    }

    handleSubmit(event) {
        event.preventDefault()
        const randNum = Math.floor(Math.random() * this.state.allMemeImgs.length)
        const randMemeImg = this.state.allMemeImgs[randNum].url
        this.setState({ randomImg: randMemeImg })
    }

    render() {
        return (
            <div className="container">
                <h1 className="text-center mb-4">Meme Generator</h1>
                <form className="row mb-4" onSubmit={this.handleSubmit}>
                    <div className="col-12 col-md-5">
                        <div className="form-group">
                        <input
                            type="text"
                            name="topText"
                            className="form-control"
                            placeholder="Top Text"
                            value={this.state.topText}
                            onChange={this.handleChange}
                        />
                        </div>
                    </div>
                    <div className="col-12 col-md-5">
                        <div className="form-group">
                        <input
                            type="text"
                            name="bottomText"
                            className="form-control"
                            placeholder="Bottom Text"
                            value={this.state.bottomText}
                            onChange={this.handleChange}
                        />
                        </div>
                    </div>
                    <div className="col-12 col-md-2 d-flex align-items-center justify-content-center">
                        <button className="btn btn-primary w-100">Gen</button>
                    </div>
                </form>

                <div className="text-center position-relative">
                    <div className="meme-container">
                        <img
                            src={this.state.randomImg}
                            alt="Meme"
                            className="img-fluid mb-2"
                            style={{ height: "400px", objectFit: "cover" }}
                        />
                        <h2
                          className="position-absolute top-0 start-0 end-0 text-center text-white"
                          style={{
                            backgroundColor: "rgba(0, 0, 0, 0)",
                            margin: "2rem 0",
                            textShadow: "2px 2px 4px rgba(0, 0, 0, 0.8)",
                          }}
                        >
                            {this.state.topText}
                        </h2>
                        <h2
                            className="position-absolute bottom-0 start-0 end-0 text-center text-white"
                            style={{
                                backgroundColor: "rgba(0, 0, 0, 0)",
                                margin: "2rem 0",
                                textShadow: "2px 2px 4px rgba(0, 0, 0, 0.8)",
                            }}
                            >
                            {this.state.bottomText}
                        </h2>
                    </div>
                </div>
            </div>
        )
    }
}

export default MemeGenerator