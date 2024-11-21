import React from "react"

function TodoItem(props) {
    const completedStyle = {
        fontStyle: "italic",
        color: "#cdcdcd",
        textDecoration: "line-through"
    }

    return (
        <div className="list-group-item d-flex gap-3">
            <input
                type="checkbox"
                checked={props.item.completed}
                onChange={() => props.handleChange(props.item.id)}
                className="form-check-input"
            />
            <strong style={props.item.completed ? completedStyle: null} className="form-checked-content">{props.item.text}</strong>
        </div>
    )
}

export default TodoItem